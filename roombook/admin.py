from django.contrib import admin
from .models import Room, RoomType, Booking

# Register your models here.


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'price')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'type', 'occupied')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room_number',  'check_in', 'check_out', 'is_active')
    list_filter = ('is_active', 'room_number')