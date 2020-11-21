
# Hotel Reservation System

Hotel reservation system is a sytem created with Django and Javascript for the EDX web programming with Python and Javascript online program. It has been developed using the contents of the material provided during the course, applying lessons learned from every section. This capstone project is an application of all the techniques, tools, languages and practices learned throughout the course.

## Demo

[![Quick demo](https://github.com/jorgecontreras/twovago/blob/master/reserve.png)](https://www.youtube.com/watch?v=o8aFsbYnJF4&t "Reserve App Demo")

## Tools and techniques learned and applied:

**1. Authentication.**
Most features of this project require a user to be authenticated, like the reservation feature. Authenticating the user allows to restrict and control access to the person who has the authority. This is achieved by verifying the user object before taking any action, and redirecting to the login page if applicable. In the case of asynchronous methods, the @login_required decorator is used.
 
**2. Models.**
All the content in the system is represented using models. Throughtout this project, I have made use of models to store all the information about the hotels, hotel rooms, reservations, favorites, etc. I have used foreign keys to establish constraints between hotel rooms and hotels. i have also used foreign keys in the models associated to a reservation, namely user and hotel room. I have made use of unique constraints to ensure that the system does not get duplicate reservations, allowing only one record with the same combination of user, room, checkin and checkout. The same unique constraint is applied to favorites model, to ensure there is at most one association between a user and a hotel. Finally, in order to better display the contents of the model in the Django admin, I have added a __str__() method to applicable models.

**3. Asynchronous communication between client and server** 
The application allows the user to interact with the page without requiring full page reloads. The system allows to mark hotels as favorites, make reservations and cancel reservations using Javascript for a richer user experience, avoiding full page reloads which take longer and consume more bandwidth.

**4. Django Admin.**
 The django admin is a built-in administrator interface that allows to manage, create, update, retrieve and delete (CRUD) the contents on the database. In this project, I have made use of this feature to provide the admin user with content management capabilities.

**5. Bootstrap.**
 Bootstrap is a great complement to any website, as it allows to improve the presentation and aesthetics of any page. In this project, I have used bootstrap to implement date picker for the reservations page, listings for the hotel search results, labels, alert messages, badges and more.

**6. Templating language.**
The templating language allows to interpret variables returned by the server and insert them or take decisions in the UI based on those values. I have made use of the templating language to iterate over a list of hotels and list of rooms. This template language was used also to toggle favorite icon, to make the links dynamic and more.

# Specifications

## 1. List all hotels

The starting page will display all available hotels. A search form appears on top of the screen, where the user can narrow down the list of hotels based on destination.

## 2. Search hotel by city.

The user can search hotels based on destination. He should get results for hotels based in the provided city, even if the city name is not complete. E.g. Searching for "New", would return hotels from New York City, including price per room. The hotel can have many rooms and prices vary per room. If there is more than one room, the page will display the lowest price of all the availble rooms. The listing in this page will also include a short description of the hotel.

## 3. Hotel page.

When the user clicks on any of the available hotels, he will be taken to a separate page displaying all available rooms for the hotel, eachwith a short description and its price per night. At the top of the page, the hotel name and address is displayed. A button/icon to favorite the hotel is also shown next to the hotel name.

## 4. Reservation page.

If the user is authenticated and clicks on any of the available rooms for the hotel, the user will be taken to a new page with all the details of the room, including photo. If the user is not authenticated, he will be redirected to a login page. From the reservations page, the user is able to select a checkin and checkout dates for his stay using a date picker. If the checkout date is on or before the checkin date, the user will get an alert and the reservation won't be processed. Clicking on Reserve button will trigger an asynchronous call to the server to register the reservation for the user. The user will receive a message in the screen, letting him know that the reservation is complete, or indicating an error if it failed for any reason.

## 5. Reservations List.

Clicking on the My Reservations link from the top menu will take the user to a different page where reservations can be managed. Clicking on any reservations from the list will take the user to a different page when the reservation can be managed.

## 6. Cancel reservation.

The logged user is able to cancel any reservation that was created with his account. This can be done from the reservation page.  When clicking on the "Cancel Reservation" button, the user will get a dialog to confirm that the reservation will be canceled. When back on the list of reservation, the canceled reservation will indicate so.

## 7. Favorite.

The user can mark his favorite hotels. When on the hotel page, the user should be able to click a heart icon next to the hotel name, to toggle if it's a favorite or not. Clicking on this icon will trigger a call to the server and the icon will change color to indicate wether the hotel is a favorite or not.

## 8. Favorites page.

The hotels that have been marked as favorite will be displayed in the Favorites section, accesible from the top menu. This will display only for logged in users. If there are no hotels marked as favorite, the page should indicate that.

## 9. Admin.

The user can search hotels based on destination. He should get results for hotels based in the provided city, even if the city name is not complete. E.g. Searching for "New", would return hotels from New York City.
