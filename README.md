# Taxi Booking Console Application

This project is a simple console-based taxi booking system built in Python. It allows users to register, log in, search for taxis by pickup location, and book a taxi. An admin can also add taxis and view their profile.

## Features

- User registration and login
- Admin login using a predefined admin account
- Taxi search based on pickup location
- Taxi booking flow for registered users
- Basic profile viewing for users and admin
- Custom exception handling for invalid menu choices

## Project Structure

- main.py: Entry point of the application
- Models/: Contains classes for User, Admin, Taxi, and Booking
- Services/: Contains business logic for users, admin, taxis, and bookings
- Utils/: Contains ID generators for users, taxis, and bookings
- Exceptions/: Contains custom exceptions used in the app

## How It Works

1. The application starts in the main menu.
2. Users can choose to log in, register, or exit.
3. After logging in, users can search for taxis in their pickup area and proceed to booking.
4. The admin can add taxis to the system.
5. Booking updates the taxi's location to the drop location.

## How to Run

From the project folder, run:

```bash
python3 main.py
```

## Notes

- This application uses in-memory storage, so data is lost when the program exits.
- It is a beginner-friendly project that demonstrates object-oriented programming and console-based interaction in Python.