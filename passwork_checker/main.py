#Password Valdatoir, Elisheva Kibbie 

import re

def check_password():
    while True:
<<<<<<< HEAD
        # Asks user for their password
=======
        # Asks user for their password (*/ω＼*)
>>>>>>> 9f0e9791b98280c3ea5346a190b17f94ecebfe7d
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

check_password()