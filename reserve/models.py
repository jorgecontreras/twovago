from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class City(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    address = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="city")

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    image = models.CharField(max_length=512, blank=True)
    price = models.FloatField(default=1.00)
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name="hotel_room", default=0)

    def __str__(self):
        return self.name + " - " + str(self.hotel)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user")
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name="favorite_hotel")

    class Meta:
        unique_together = ('user', 'hotel')

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_reservation")
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name="room_reserved")
    checkin = models.DateField()
    checkout = models.DateField()
    status = models.CharField(max_length=16, default="", blank=True)

    class Meta:
        unique_together = ('user', 'room', 'checkin', 'checkout')

    def __str__(self):
        return str(self.user) + ": " + str(self.room) 