# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:26:32 2024

@author: Austin
"""

miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons of gas used: "))

miles_per_gallon = round(miles_driven / gallons_used, 2)

print(f"The miles per gallon rating for this trip is {miles_per_gallon}")



