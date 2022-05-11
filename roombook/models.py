from django.db import models
from django.conf import settings



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


    def __str__(self):
        return f"{self.user} has booked  Room {self.room_number} from {self.check_in} to {self.check_out}"
