# Generated by Django 3.1 on 2020-11-03 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0002_city_favorite_hotel_hotelrooms_reservation_review_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='hotel_room', to='reserve.hotel'),
        ),
        migrations.DeleteModel(
            name='HotelRooms',
        ),
    ]
