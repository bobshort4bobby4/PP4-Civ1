""" 
roombook unit tests
"""


from django.test import TestCase, Client
from forms.forms import AvailabilityForm
from home.views import HomeView
from .models import RoomType, Room, Booking
from django.test import tag
from booking_code.check_availability import check_availability
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.admin.sites import AdminSite
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
import json
from datetime import datetime, timedelta, date
from .admin import RoomTypeAdmin




@tag('forms')
class TestAvailabilityForm(TestCase):

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
        self.assertEqual(form.errors['check_out'][0], 'This field is required.')

    def test_only_twofields_are_shown_onform(self):
        # check no other fields have been added to form
        form = AvailabilityForm()
        self.assertEqual(form.Meta.fields, ['check_in', 'check_out'])


@tag('views')
class TestRoombookViews(TestCase):

    def test_availabilityview_get_renders_correct_template(self):
        #  creates an correct instance of RoomType and checks correct template rendered
        item = RoomType.objects.create(type='Single', description='blahblah', price=10, occupancy=1,image_url='', image='')
        response = self.client.get(f'/roombook/book_1/{ item.type}/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'roombook/book_1.html')

    def test_availabilityview_get_renders_correct_template_if_type_wrong(self):
        # creates an incorrect instance of RoomType and checks correct template rendered
        item = RoomType.objects.create(type='wrong', description='blahblah', price=10, occupancy=1,image_url='', image='')
        response = self.client.get(f'/roombook/book_1/{ item.type}/')
        # print(response.context)
        self.assertNotEqual(response.status_code,200)
        self.assertRedirects(response, reverse('home:home'))
        

    def test_bookview_get_renders_correct_template(self):
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10, occupancy=1) 
        itemtype.save()

        # create instance of Room                                          
        roomnum = Room(room_number=2, type=itemtype)
        roomnum.save()

         # create User instance
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='brian',
                                                   password='dogs12')

        context = {
                        'user':self.user,
                        'room_number':roomnum,
                        'check_in':'2022-05-01',
                        'check_out':'2022-05-03',
                        'is_active':True,
            }
        response = self.client.get(f'/roombook/book/', context)
        # print(response.context)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'roombook/book.html')




    def test_availabilityview_post_redirects_if_type_incorrect(self):# does not work
       
         # create instance of RoomType
        itemtype = RoomType(type='wrong', price=10, occupancy=1) 
        itemtype.save()

        # create instance of Room                                          
        roomnum = Room(room_number=2, type=itemtype)
        roomnum.save()

         # create User instance
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='brian',
                                                   password='dogs12')
        booking = {
                        'user':self.user,
                        'room_number':roomnum,
                        'check_in':'2022-05-01',
                        'check_out':'2022-05-03',
                        'is_active':True,
            }
        # post request with type incorrect should redirect to home page
        response= self.client.post(f'/roombook/book',booking)
        self.assertNotEqual(response.status_code, 200)
        # self.assertRedirects(response, reverse('home:home'))
       



 
@tag('models')
class TestRoomBookModels(TestCase):

    def test_item_string_method_returns_type_for_roomtype_model(self):
        # create sample row of RoomType table and compare to expected output
        item = RoomType.objects.create(type='Single', description='blahblah', price=10, image_url='', image='')
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
        item = Booking.objects.create(user=self.user, room_number=roomnum , check_in='2022-02-01', check_out='2022-02-03', is_active=True)
        self.assertEqual(str(item),'brian has booked  Room 2 from 2022-02-01 to 2022-02-03')
       

@tag('admin')
class TestAdminSite(TestCase):

    def test_occupancy14_rate_function_is_correct(self):
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10, occupancy=1) 
        itemtype.save()
        # create User instance
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='brian',
                                                   password='dog12')
                                               
       
        # instance of admin 
        self.roomtypemodeladmin = RoomTypeAdmin(model=RoomType, admin_site=AdminSite())

        # create 10 instances of Room   
        num_of_rooms = 10
        for num in range(num_of_rooms):
            roomnum =Room(room_number=num, type=itemtype)
            roomnum.save()
        rooms = Room.objects.all()
        
        # ten rooms for 14 nights means 140 possible nights if i book 14 nighs occ rate shoudl be 10%
        roominstance = Room.objects.get(pk=1)
       
        today = date.today()
        Booking.objects.create(
                                user = self.user, 
                                room_number= roominstance,
                                check_in= today,
                                check_out= today + timedelta(days=14),
                                is_active= True   
                                 )

        bookings = Booking.objects.all()
        print(len(bookings))
        
          # prepare client
        User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        c = Client()
        c.login(username='superuser', password='secret')                

    

        #run test
        response = self.roomtypemodeladmin.occupancy_14_Days(itemtype)
        
        self.assertEqual(response,'10.0')
        


    def test_occupancy30_rate_function_is_correct(self):
            # create instance of RoomType
            itemtype = RoomType(type='Single', price=10, occupancy=1) 
            itemtype.save()
            # create User instance
            user_model = get_user_model()
            self.user = user_model.objects.create_user(username='brian',
                                                    password='dog12')
            # create 10 instance of Room                                          
        
            # instance of admin 
            self.roomtypemodeladmin = RoomTypeAdmin(model=RoomType, admin_site=AdminSite())

            num_of_rooms = 10
            for num in range(num_of_rooms):
                roomnum =Room(room_number=num, type=itemtype)
                roomnum.save()
            rooms = Room.objects.all()
            
            # ten rooms for 30 nights means 300 possible nights if i book 30 nights occ rate shoudl be 10%
            roominstance = Room.objects.get(pk=1)
        
            today = date.today()
            Booking.objects.create(
                                    user = self.user, 
                                    room_number= roominstance,
                                    check_in= today,
                                    check_out= today + timedelta(days=30),
                                    is_active= True   
                                    )

            bookings = Booking.objects.all()
            print(len(bookings))
            
            # prepare client
            User.objects.create_superuser(
                username='superuser', password='secret', email='admin@example.com'
            )
            c = Client()
            c.login(username='superuser', password='secret')                

        

            #run test
            response = self.roomtypemodeladmin.occupancy_30_Days(itemtype)
            
            self.assertEqual(response,'10.0')
