# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('restaurant_booking')


def get_name():
    """
    Gets the name for the booking from user input.
    """
    global FULL_NAME
    print("Please enter your full name for the booking.\n")
    while True:
        first_name = input("Please enter your First name: \n")
        if validate_name(first_name):
            break
    while True:
        last_name = input("Please enter your Last name: \n")
        if validate_name(last_name):
            break
    FULL_NAME = f"{first_name.capitalize()} {last_name.capitalize()}"
    print(f"Thank you {FULL_NAME}")
    return FULL_NAME


def validate_name(name_input):
    """
    Validates user-input for name
    Passes only when the user has submitted a name
    """
    if name_input == "":
        print("Name is required\n")
        return False
    elif name_input.isnumeric():
        print(f"Must be letters only.'{name_input}' is wrong.")
        return False
    elif not name_input.isalpha():
        print(f"Must be letters only.'{name_input}' is wrong.\n")
        return False
    else:
        return True
    return True


def get_people():
    """
    Gets the amount of people for the booking.
    """
    print("\nHow many people are you booking for?")
    while True:
        try:
            people_input = int(input("Enter amount here: \n"))
        except ValueError:
            print("Not an number! Try again.")
            continue
        else:
            print(f"Booking for {people_input} people.")
            return people_input
            break


def update_bookings_worksheet():
    """
    Update bookings worksheet, add new row with the list data provided
    """
    print("Updating bookings worksheet...\n")
    bookings_worksheet = SHEET.worksheet("bookings")
    bookings_worksheet.append_row(data)
    print("Bookings worksheet updated successfully.\n")
    print("Your booking is now confirmed.")
    print("To make another booking press the 'run programme' button.")


print("Welcome to the restaurant booking system.\n")
name = get_name()
people = get_people()
data = name, people
update_bookings_worksheet()
