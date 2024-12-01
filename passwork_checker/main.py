#Password Valdatoir, Elisheva Kibbie 

import re

def check_password():
    while True:
        # Prompt user for password input
        password = input("Enter your password: ")

        # Check if password is at least 8 characters long
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

        # If all checks pass, accept the password
        print("Password accepted!")
        break