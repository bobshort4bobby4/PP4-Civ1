"""
routing paths for home app
"""
from django.urls import path
from .views import HomeView, InfoView, StaffView, approvereview


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('info/', InfoView.as_view(), name='info'),
    path('staff/', StaffView.as_view(), name='staff'),
    path('approve/<pk>', approvereview, name='approve')

]
