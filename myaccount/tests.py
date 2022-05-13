from django.test import TestCase, Client
from django.test import tag
from django.urls import reverse
from roombook.models import Room, RoomType, Booking
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date


@tag('views')
class TestmyaccountView(TestCase):

    def test_extend_booking_uses_correct_template(self):

        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
              # create instance of RoomType
        itemtype = RoomType(type='Single', price=10, occupancy=1) 
        itemtype.save(force_insert=True)

        # create instance of Room                                          
        roomnum = Room(room_number=2, type=itemtype)
        roomnum.save(force_insert=True)



        self.booking = Booking.objects.create(user=test_user, room_number= roomnum, check_in='2022-05-10',check_out='2022-05-21', is_active=True) 
        response = self.client.get(f'/myaccount/extend/{self.booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myaccount/extend_booking.html')

       
    def test_cancel_booking_redirects_if_noticeperiod_too_short(self):
        today = date.today()
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10, occupancy=1) 
        itemtype.save(force_insert=True)

        # create instance of Room                                          
        roomnum = Room(room_number=2, type=itemtype)
        roomnum.save(force_insert=True)

        # create invalid check-in date 
        invalid_date = today + timedelta(days=2)

        # create booking entry with invalid check in date
        self.booking = Booking.objects.create(user=test_user, room_number= roomnum, check_in=invalid_date, check_out='2022-05-21', is_active=True)
        response = self.client.get(f'/myaccount/cancel/{self.booking.id}')
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, '/myaccount/myaccount/')
        

    def test_cancel_booking_redirects_if_check_in_past_tense(self):
        today = date.today()
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10, occupancy=1) 
        itemtype.save(force_insert=True)

        # create instance of Room                                          
        roomnum = Room(room_number=2, type=itemtype)
        roomnum.save(force_insert=True)

        # create invalid check-in date 
        invalid_date = today - timedelta(days=2)

        # create booking entry with invalid check in date
        self.booking = Booking.objects.create(user=test_user, room_number= roomnum, check_in=invalid_date, check_out='2022-05-21', is_active=True)
        response = self.client.get(f'/myaccount/cancel/{self.booking.id}')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "myaccount/myaccount.html")



    def test_cancel_booking_displays_correct_template_if_notice_over7days(self):
        today = date.today()
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        # create instance of RoomType
        itemtype = RoomType(type='Single', price=10, occupancy=1) 
        itemtype.save(force_insert=True)

        # create instance of Room                                          
        roomnum = Room(room_number=2, type=itemtype)
        roomnum.save(force_insert=True)

        # create valid check-in date 
        valid_date = today + timedelta(days=9)

        # create booking entry with valid check in date
        self.booking = Booking.objects.create(user=test_user, room_number= roomnum, check_in=valid_date, check_out='2022-05-21', is_active=True)
        response = self.client.get(f'/myaccount/cancel/{self.booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "myaccount/cancel_booking.html")

