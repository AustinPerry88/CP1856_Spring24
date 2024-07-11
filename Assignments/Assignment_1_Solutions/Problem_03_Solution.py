# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:51:23 2024

@author: Arun.Rameshbabu
"""

# Display a welcome message
print("Travel Time Calculator")
print()

# Get input from the user
miles = int(input("Enter miles: "))
miles_per_hour = int(input("Enter miles per hour: "))
print()

# Perform the calculations
hours = miles // miles_per_hour
minutes = miles % miles_per_hour

# Display the results
print("Estimated travel time")
print("Hours:", hours)
print("Minutes:", minutes)
