# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:47:29 2024

@author: Arun.Rameshbabu
"""

# Display a welcome message
print("Registration Form")
print()

# Get input from the user
first_name = input("First name:\t")
last_name = input("Last name:\t")
birth_year = input("Birth year:\t")
print()

# Create strings
name = f"{first_name} {last_name}"
temp_password = f"{first_name}*{birth_year}"

# Display the results
print(f"Welcome {name}!")
print("Your registration is complete.")
print(f"Your temporary password is: {temp_password}")
    