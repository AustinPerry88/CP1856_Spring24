# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:49:49 2024

@author: Arun.Rameshbabu
"""

# Display a welcome message
print("Pay Check Calculator")
print()

# Get input from the user
hours = float(input("Hours Worked:\t\t"))
pay_rate = float(input("Hourly Pay Rate:\t"))
print()

# Make calculations
gross_pay = round(hours * pay_rate, 2)
tax_rate = 18
tax_amount = round(gross_pay * (tax_rate / 100), 2)
take_home_pay = round(gross_pay - tax_amount, 2)

# Display the results
print("Gross Pay:\t\t", gross_pay)
print("Tax Rate:\t\t", str(tax_rate) + "%")
print("Tax Amount:\t\t", tax_amount)
print("Take Home Pay:\t\t", take_home_pay)
   