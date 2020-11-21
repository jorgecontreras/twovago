
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("hotel/<int:hotel_id>", views.view_hotel, name="view_hotel"),
    path("reserve/<int:room_id>", views.reserve, name="reserve"),
    path("cancel/<int:reservation_id>", views.cancel, name="cancel"),
    path("reservation/<int:reservation_id>", views.view_reservation, name="view_reservation"),
    path("reservations", views.reservations_list, name="reservations_list"),
    path("favorite/<int:hotel_id>", views.favorite, name="favorite"),
    path("favorites", views.favorites, name="favorites"),
    path("search", views.index, name="search")
]
