from django.urls import path
from .views import HomeView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # path('info/', InfoView.as_view(), name='info'),
    # path('contact/', ContactView.as_view(), name='contact'),
]