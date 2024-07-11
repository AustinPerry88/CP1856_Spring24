# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:54:02 2024

@author: Arun.Rameshbabu
"""

# Display a welcome message
print("Tip Calculator")
print()

# Get input from the user
meal_cost = float(input("Cost of meal: "))
print()

for tip_percent in range(15, 30, 5):
    print(f"{tip_percent}%")

    # Calculate tip and total amount
    tip_percent = tip_percent / 100
    tip_amount = round(meal_cost * tip_percent, 2)
    total = round(meal_cost + tip_amount, 2)

    # Display the results
    print("Tip amount:  ", tip_amount)
    print("Total amount:", total)
    print()
