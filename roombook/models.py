"""
Models for Roombook app
"""
from datetime import date
from django.db import models
from django.conf import settings


class MarkOutDatedAsInactive(models.Manager):
    """
    Custom model manager
    """

    def set_inactive(self, bookings):
        """
        determines if the booking is past-tense and changes the
        is_active field to false if so

        Parameters: Queryset of all instances of booking relation

        Return: ammended bookings
        """
        today = date.today()

        for booking in bookings:
            if booking.check_out < today:
                booking.is_active = False
                booking.save()
        return bookings

    def all(self):
        """
         Override ll function to include custom function
        """
        bookings = super().all()
        bookings = self.set_inactive(bookings)
        return bookings


class RoomType(models.Model):
    """
    Define RoomType relation structure
    """
    Room_Types = (
        ('Single', 'Single'),
        ('Queen', 'Queen'),
        ('Double', 'Double'),
    )

    type = models.CharField(max_length=6, null=False, choices=Room_Types)
    description = models.TextField(max_length=250, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.type}'


class Room(models.Model):
    """
    Define Room relation structure
    """

    room_number = models.IntegerField()
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room_number}'


class Booking(models.Model):
    """
    Define Booking relation structure
    """
    user = models.ForeignKey(
                            settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)
    is_active = models.BooleanField(default=True)

    objects = MarkOutDatedAsInactive()

    def __str__(self):
        return f"{self.user} has booked Room {self.room_number} from {self.check_in} to {self.check_out}"
