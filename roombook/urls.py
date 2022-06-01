
"""
 Url pathd for roombook app
"""
from django.urls import path
from .views import availability_view, book_room_view


app_name = 'roombook'


urlpatterns = [
    # path('book_1/<type>/', AvailabilityView.as_view(), name="book_1"),
    path('book_1/<type>/', availability_view, name="book_1"),
    path('book/', book_room_view, name="book"),
]
