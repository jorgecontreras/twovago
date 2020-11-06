# Reservations
Hotel reservation system

## Demo

[![Quick demo](https://github.com/jorgecontreras/twovago/blob/master/reserve.png)](https://www.youtube.com/watch?v=o8aFsbYnJF4&t "Reserve App Demo")

# Specifications

## 1. List all hotels

The starting page will display all available hotels. A search form appears on top of the screen, where the user can narrow down the list of hotels based on destination.

## 2. Search hotel by city.

The user can search hotels based on destination. He should get results for hotels based in the provided city, even if the city name is not complete. E.g. Searching for "New", would return hotels from New York City.

## 3. Hotel page.

When the user clicks on any of the available hotels, it will be taken to a separate page with additional information about the rooms of that hotel, along with its price per night.

## 4. Reservation page.

If the user clicks on any of the available rooms for the hotel, it will be taken to a new page with all the details of the room, including photo. The user is able to select a checkin and checkout dates for his stay. If the checkout date is on or before the checkin date, the user will get an alert and the reservation won't be processed.

## 5. Cancel reservation.

The user is able to cancel any reservation that was created with his account. This can be done from the reservation page. The user will get a dialog to confirm that the reservation will be canceled. When back on the list of reservation, the canceled reservation will indicate so.

## 6. Favorite.

The user can mark his favorite hotels. When on the hotel page, the user should be able to click a heart icon next to the hotel name, to toggle if it's a favorite or not. This will be accomplished with Javascript to avoid a reload of the full page.

## 7. Favorites page.

The hotels that have been marked as favorite will be displayed in the Favorites section, accesible from the top menu. This will display only for logged in users. If there are no hotels marked as favorite, the page should indicate that.

## 8. Admin.

All the hotels, rooms and cities are managed with the built-in Django admin. 
