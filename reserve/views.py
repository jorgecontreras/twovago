import json
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import dateutil.parser

from .models import User, Hotel, Room, Reservation, Favorite, City

class SearchForm(forms.Form):
    destination = forms.CharField(label='')

def index(request):

    user = request.user 

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            destination = form.cleaned_data["destination"]
            destination = destination.strip().lower()

        if destination != "":
            city = City.objects.filter(name__contains=destination).first()
            hotels = Hotel.objects.filter(city=city).all()
        else:
            hotels = Hotel.objects.all()

    else:
        hotels = Hotel.objects.all()

    for hotel in hotels:
        # get lowest rate
        room = Room.objects.filter(hotel=hotel).order_by("price").first()
        if room:
            hotel.rate = '${:.2f}'.format(room.price)
        else:
            hotel.rate = 'call for price'
    return render(request, "reserve/index.html", {
        "hotels": hotels,
        'form': SearchForm()
    })

def view_hotel(request, hotel_id):
    user = request.user

    hotel = Hotel.objects.filter(id=hotel_id).first()
    rooms = Room.objects.filter(hotel=hotel_id).all()
    favorite = None
    if not user.is_anonymous:
        fav = Favorite.objects.filter(hotel=hotel, user=user).first()
        if fav is not None:
            favorite = True

    return render(request, "reserve/hotel.html", {
        "hotel": hotel,
        "rooms": rooms,
        "favorite": favorite
    })

@login_required
@csrf_exempt
def reserve(request, room_id):
    user = request.user

    if user.is_anonymous:
        return HttpResponseRedirect('/login')

    if request.method == "POST":
        #parse request data
        data = json.loads(request.body)
        checkin = data.get("checkin").strip() 
        checkout = data.get("checkout").strip() 
        checkin_date = dateutil.parser.parse(checkin)
        checkout_date = dateutil.parser.parse(checkout)

        #validate dates
        if checkin_date >= checkout_date:
            return JsonResponse({
                "status": "fail",
                "message": "error: please verify dates."
            })

        try:
            room = Room.objects.filter(id=room_id).first()
            r = Reservation(user=user, checkin=checkin_date, checkout=checkout_date, room=room)
            r.save()
            status = 'success'
            message = "<b>We are happy to have you, " + user.username + "!</b><br> Your reservation is complete."
        except:
            status= 'fail'
            message = "<b>something is not quite right. </b><br> we apologize or the inconvenience."
        return JsonResponse({
            "status": status,
            "message": message
        })

    room = Room.objects.filter(id=room_id).first()
    hotel = Hotel.objects.filter(id=room.hotel.id).first()

    return render(request, "reserve/room.html", {
        "hotel": hotel,
        "room": room
    })

def reservations_list(request):
    user = request.user

    if user.is_anonymous:
        return HttpResponseRedirect('/login')

    reservations = Reservation.objects.filter(user=user).all()

    return render(request, "reserve/reservations.html", {
        "reservations" : reservations
    })

def view_reservation(request, reservation_id):
    user = request.user

    if user.is_anonymous:
        return HttpResponseRedirect('/login')

    try:
        reservation = Reservation.objects.filter(user=user, id=reservation_id).first()
    except:
        reservation = None

    return render(request, "reserve/reservation.html", {
        "reservation" : reservation
    })

@login_required
@csrf_exempt
def cancel(request, reservation_id):
    user = request.user

    if user.is_anonymous:
        return HttpResponseRedirect('/login')

    try:
        reservation = Reservation.objects.filter(user=user, id=reservation_id).first()
        reservation.status = 'canceled'
        reservation.save()
        status = "success"
        message = "your reservation has been canceled."
    except:
        status = "fail"
        message = "we are having trouble canceling your reservation at this moment. sorry for the inconvenience"
    return JsonResponse({
            "status": status,
            "message": message
        })

@login_required
@csrf_exempt
def favorite(request, hotel_id):
    user = request.user

    if request.method != "POST":
        return JsonResponse({"error": "POST is required"}, status=400)

    try:
        favorite = Favorite.objects.filter(user=user, hotel=hotel_id).first()
    except:
        favorite = None

    # mark it as favorite
    if favorite is None:
        try:
            hotel = Hotel.objects.filter(id=hotel_id).first()
            favorite = Favorite(user=user, hotel=hotel)
            favorite.save()
            favorite = True
        except:
            favorite = False
    #remove from favorites
    else:
        favorite.delete()
        favorite = False

    return JsonResponse({
        "status": "success",
        "favorite": favorite
    }, status=200)

def favorites(request):
    user = request.user

    favorites = Favorite.objects.filter(user=user).all().values_list('hotel_id', flat=True)

    hotels = Hotel.objects.filter(id__in=favorites)

    for hotel in hotels:
        # get lowest rate
        room = Room.objects.filter(hotel=hotel).order_by("price").first()
        if room:
            hotel.rate = '${:.2f}'.format(room.price)
        else:
            hotel.rate = 'call for price'
    return render(request, "reserve/favorites.html", {
        "hotels": hotels
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "reserve/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "reserve/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "reserve/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "reserve/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "reserve/register.html")
