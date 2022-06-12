"""
roombook unit tests
"""


from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite
from django.urls import reverse
from datetime import timedelta, date
from django.test import tag
from django.test import TestCase
from forms.forms import AvailabilityForm
from .models import RoomType, Room, Booking

from .admin import RoomTypeAdmin


@tag('forms')
class TestAvailabilityForm(TestCase):
    """
    tests for forms
    """

    def test_checkin_required(self):
        # create form field with blank value
        form = AvailabilityForm({'check_in': ''})
        # check if form valid,error in correct field and correct error produced
        self.assertFalse(form.is_valid())
        self.assertIn('check_in', form.errors.keys())
        self.assertEqual(form.errors['check_in'][0], 'This field is required.')

    def test_checkout_required(self):
        # create form field with blank value
        form = AvailabilityForm({'check_out': ''})
        # check if form valid,error in correct field and correct error produced
        self.assertFalse(form.is_valid())
        self.assertIn('check_out', form.errors.keys())
        self.assertEqual(
            form.errors['check_out'][0], 'This field is required.')

    def test_only_twofields_are_shown_onform(self):
        # check no other fields have been added to form
        form = AvailabilityForm()
        self.assertEqual(form.Meta.fields, ['check_in', 'check_out'])


@tag('views')
class TestRoombookViews(TestCase):
    """
    Tests for roombook views
    """

    def test_availabilityview_get_renders_correct_template(self):
        #  creates an correct instance of RoomType
        #  and checks correct template rendered
        item = RoomType.objects.create(
                                        type='Single',
                                        description='blahblah',
                                        price=10,
                                        image_url='',
                                        image='')
        response = self.client.get(f'/roombook/book_1/{ item.type}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roombook/book_1.html')

    def test_availabilityview_get_renders_correct_template_if_type_wrong(self):
        # creates an incorrect instance of RoomType
        #  and checks correct template rendered
        item = RoomType.objects.create(
                                        type='wrong',
                                        description='blahblah',
                                        price=10,
                                        image_url='',
                                        image='')
        response = self.client.get(f'/roombook/book_1/{ item.type}/')
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('home:home'))

    def test_bookview_get_renders_correct_template(self):
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10)
        itemtype.save()

        # create instance of Room
        roomnum = Room(room_number=2, type=itemtype)
        roomnum.save()

        # create User instance
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='brian',
                                                   password='dogs12')

        context = {
                        'room_number': str(roomnum.room_number),
                        'check_in': '2022-05-01',
                        'check_out': '2022-05-03',
                        'is_active': True,
                        'type': 'Single',
            }
        # set session database 'data' value to context
        session = self.client.session
        session['data'] = context
        session.save()
        response = self.client.get('/roombook/book/', context)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roombook/book.html')


@tag('models')
class TestRoomBookModels(TestCase):
    """
    Tests for roombook app models
    """

    def test_item_string_method_returns_type_for_roomtype_model(self):
        # create sample row of RoomType table and compare to expected output
        item = RoomType.objects.create(
                                        type='Single',
                                        description='blahblah',
                                        price=10,
                                        image_url='',
                                        image='')
        self.assertEqual(str(item), 'Single')

    def test_item_string_method_returns_roomnumber_for_room_model(self):
        itemtype = RoomType(type='Single', price=10)
        itemtype.save()
        item = Room.objects.create(room_number=10, type=itemtype)
        self.assertEqual(str(item), '10')

    def test_item_string_method_returns_correct_string_for_booking_model(self):
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10)
        itemtype.save()
        # create User instance
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='brian',
                                                   password='dogskin12')
        # create instance of Room
        roomnum = Room(room_number=2, type=itemtype)
        roomnum.save()
        # create sample Booking table row and compare with expected output
        item = Booking.objects.create(
                                        user=self.user,
                                        room_number=roomnum,
                                        check_in='2022-02-01',
                                        check_out='2022-02-03',
                                        is_active=True)
        self.assertEqual(
            str(item), 'brian has booked Room 2 from 2022-02-01 to 2022-02-03')


@tag('admin')
class TestAdminSite(TestCase):
    """
    Tests for admin functions
    """

    def setUp(self):

        # create instance of RoomType
        self.itemtype = RoomType(type='Single', price=10)
        self.itemtype.save()

        # create User instance
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='brian',
                                                   password='dog12')

        # instance of admin
        self.roomtypemodeladmin = RoomTypeAdmin(
                                                model=RoomType,
                                                admin_site=AdminSite())
        # create 10 instances of Room
        num_of_rooms = 10
        for num in range(num_of_rooms):
            roomnum = Room(room_number=num, type=self.itemtype)
            roomnum.save()

        self.today = date.today()

    def test_occupancy14_rate_function_is_correct(self):
        """
        test that ocupancy rate for 14 days is calculated correctly
        """
        # ten rooms for 14 nights means 140 possible nights
        #  if i book 14 nights occupancy rate should be 10%
        roominstance = Room.objects.get(pk=1)

        Booking.objects.create(
                                user=self.user,
                                room_number=roominstance,
                                check_in=self.today,
                                check_out=self.today + timedelta(days=14),
                                is_active=True
                                 )

        # run test
        response = self.roomtypemodeladmin.occupancy_14_Days(self.itemtype)

        self.assertEqual(response, '10.0')

    def test_occupancy30_rate_function_is_correct(self):
        """
        test that ocupancy rate for 30 days is calculated correctly
        """

        # instance of admin
        self.roomtypemodeladmin = RoomTypeAdmin(
                                                model=RoomType,
                                                admin_site=AdminSite())

        # ten rooms for 30 nights means 300 possible nights
        #  if i book 30 nights occ rate shoudl be 10%
        roominstance = Room.objects.get(pk=1)

        Booking.objects.create(
                                user=self.user,
                                room_number=roominstance,
                                check_in=self.today,
                                check_out=self.today + timedelta(days=30),
                                is_active=True
                                )

        # run test
        response = self.roomtypemodeladmin.occupancy_30_Days(self.itemtype)

        self.assertEqual(response, '10.0')
