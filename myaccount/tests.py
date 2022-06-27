"""
tests for myaccount app
"""
from datetime import timedelta, date
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase, Client
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
        self.user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10)
        itemtype.save(force_insert=True)

        # create instance of Room
        self.roomnum = Room(room_number=2, type=itemtype)
        self.roomnum.save(force_insert=True)

        self.today = date.today()
        c = Client()
        self.user.is_superuser = True
        self.user.save()
        self.logged_in = c.login(username='testuser', password='testpw')
        self.client.force_login(self.user)
        self.assertTrue(self.logged_in)

    def test_extend_booking_uses_correct_template(self):
        self.bookid = Booking.objects.create(
                                                user=self.user,
                                                room_number=self.roomnum,
                                                check_in='2022-05-10',
                                                check_out='2022-05-21',
                                                is_active=True)
        self.assertTrue(self.logged_in)
        response = self.client.get(f'/myaccount/extend/{self.bookid.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myaccount/extend_booking.html')

    def test_cancel_booking_redirects_if_noticeperiod_too_short(self):

        # create invalid check-in date
        invalid_date = self.today + timedelta(days=2)

        # create booking entry with invalid check in date
        self.booking = Booking.objects.create(
                                                user=self.user,
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
                                                user=self.user,
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
                                                user=self.user,
                                                room_number=self.roomnum,
                                                check_in=valid_date,
                                                check_out='2022-05-21',
                                                is_active=True,)

        c = Client()
        c.login(username='testuser', password='testpw')
        response = self.client.get(f'/myaccount/cancel/{self.booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "myaccount/cancel_booking.html")

    def test_cancel_booking_redirects_correctly_if_notice_under7days(self):

        # create invalid check-in date
        invalid_date = self.today + timedelta(days=1)

        # create booking entry with invalid check in date
        self.booking = Booking.objects.create(
                                                user=self.user,
                                                room_number=self.roomnum,
                                                check_in=invalid_date,
                                                check_out='2022-05-21',
                                                is_active=True,)

        c = Client()
        c.login(username='testuser', password='testpw')
        response = self.client.get(f'/myaccount/cancel/{self.booking.id}')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('myaccount:myaccount'))
