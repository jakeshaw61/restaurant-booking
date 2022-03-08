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