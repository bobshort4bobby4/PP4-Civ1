from django.urls import path
from .views import HomeView, InfoView, StaffView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('info/', InfoView.as_view(), name='info'),
    path('staff/', StaffView.as_view(), name='staff'),
    
]