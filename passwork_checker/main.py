#Password Valdatoir, Elisheva Kibbie 

import re

def check_password():
    while True:
        # Asks user for their password (*/ω＼*)
        password = input("Enter your password: ")

        # Check if password is long enough ᓚᘏᗢ
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue

        # Check if password contains at least one number
        if not re.search(r'\d', password):
            print("Password must contain at least one number.")
            continue

        # Check if password contains at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("Password must contain at least one special character (@, #, $, %, *, &).")
            continue

        # gives the these words is the password is accepted
        print("Password accepted!")
        break