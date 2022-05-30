"""
tests for myaccount app
"""
from django.contrib.auth.models import User
from datetime import timedelta, date
from django.test import TestCase
from django.test import tag
from roombook.models import Room, RoomType, Booking


@tag('views')
class TestmyaccountView(TestCase):
    """
    Tests for the myaccount app views
    """

    def setUp(self):
        """
        common lines to all tests
        """
        self.test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10)
        itemtype.save(force_insert=True)

        # create instance of Room
        self.roomnum = Room(room_number=2, type=itemtype)
        self.roomnum.save(force_insert=True)

        self.today = date.today()

    def test_extend_booking_uses_correct_template(self):
        self.booking = Booking.objects.create(
                                                user=self.test_user,
                                                room_number=self.roomnum,
                                                check_in='2022-05-10',
                                                check_out='2022-05-21',
                                                is_active=True)

        response = self.client.get(f'/myaccount/extend/{self.booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myaccount/extend_booking.html')

    def test_cancel_booking_redirects_if_noticeperiod_too_short(self):

        # create invalid check-in date
        invalid_date = self.today + timedelta(days=2)

        # create booking entry with invalid check in date
        self.booking = Booking.objects.create(
                                                user=self.test_user,
                                                room_number=self.roomnum,
                                                check_in=invalid_date,
                                                check_out='2022-05-21',
                                                is_active=True)
        response = self.client.get(f'/myaccount/cancel/{self.booking.id}')
        self.assertEqual(response.status_code, 302)

    def test_cancel_booking_redirects_if_check_in_past_tense(self):

        # create invalid check-in date
        invalid_date = self.today - timedelta(days=2)

        # create booking entry with invalid check in date
        self.booking = Booking.objects.create(
                                                user=self.test_user,
                                                room_number=self.roomnum,
                                                check_in=invalid_date,
                                                check_out='2022-05-21',
                                                is_active=True)
        response = self.client.get(f'/myaccount/cancel/{self.booking.id}')
        self.assertEqual(response.status_code, 302)

    def test_cancel_booking_displays_correctly_if_notice_over7days(self):

        # create valid check-in date
        valid_date = self.today + timedelta(days=9)

        # create booking entry with valid check in date
        self.booking = Booking.objects.create(
                                                user=self.test_user,
                                                room_number=self.roomnum,
                                                check_in=valid_date,
                                                check_out='2022-05-21',
                                                is_active=True,)
    
        response = self.client.get(f'/myaccount/cancel/{self.booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "myaccount/cancel_booking.html")
