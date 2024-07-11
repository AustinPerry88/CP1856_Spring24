# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:52:47 2024

@author: Arun.Rameshbabu
"""

# Display a welcome message
print("Letter Grade Converter")
print()

choice = "y"
while choice.lower() == "y":

    # Get input from the user
    number = int(input("Enter numerical grade: "))

    # Convert number to letter
    if number > 87:
        letter = "A"
    elif number > 79:
        letter = "B"
    elif number > 66:
        letter = "C"
    elif number > 59:
        letter = "D"
    else:
        letter = "F"

    # Display letter
    print("Letter grade:", letter)
    print()

    # See if the user wants to continue
    choice = input("Continue (y/n)?: ")
    print()

print("Bye!")
