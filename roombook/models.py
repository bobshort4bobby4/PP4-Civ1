from django.db import models
from django.conf import settings
from datetime import datetime, date


class MarkOutDatedAsInactive(models.Manager):
    """ 
    determines if the booking is past-tense and changes the is_active field to false if so
    """

    def set_inactive(self,bookings):
        today = date.today()

        for booking in bookings:
            if booking.check_out < today:
                booking.is_active = False
                booking.save()
        return bookings

    def all(self):
        bookings = super().all() 
        bookings = self.set_inactive(bookings)
        return bookings

class RoomType(models.Model):
    Room_Types = (
        ('Single', 'Single'),
        ('Queen', 'Queen'),
        ('Double', 'Double'),
    )

    type = models.CharField(max_length=6, null=False, choices= Room_Types)
    description = models.TextField(max_length=250, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.type}'

class Room(models.Model):

    room_number = models.IntegerField()
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)
   

    def __str__(self):
        return f'{self.room_number}'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)
    is_active = models.BooleanField(default= True)

    objects = MarkOutDatedAsInactive()


    def __str__(self):
        return f"{self.user} has booked  Room {self.room_number} from {self.check_in} to {self.check_out}"
