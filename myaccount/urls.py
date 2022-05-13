from django.urls import path
from .views import ShowDetails, CancelBooking, ExtendBooking


app_name = 'myaccount'



urlpatterns = [
    path('', ShowDetails.as_view(), name="myaccount"),
    path('cancel/<pk>', CancelBooking.as_view(), name='cancel'),
    path('extend/<pk>', ExtendBooking.as_view(), name='extend'),
]