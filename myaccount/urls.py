from django.urls import path


app_name = 'myaccount'



urlpatterns = [
    path('', ShowDetails.as_view(), name="myaccount"),
    path('cancel/<pk>', CancelBooking.as_view(), name='cancel'),
    path('extend/<pk>', ExtendBooking.as_view(), name='extend'),
