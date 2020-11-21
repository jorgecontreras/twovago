from django.contrib import admin

# Register your models here.
from .models import User, Hotel, Room, Reservation, Favorite, City

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Favorite)
admin.site.register(City)