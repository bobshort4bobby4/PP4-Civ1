"""
Url path for reviews app
"""

from django.urls import path
from .views import ReviewView, CreateReview

app_name = 'reviews'

urlpatterns = [
    path('review/', ReviewView.as_view(), name='reviews'),
    path('create_review/', CreateReview.as_view(), name='create_review'),
]
