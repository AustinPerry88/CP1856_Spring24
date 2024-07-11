# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:54:39 2024

@author: Austin
"""

monthly_invest = int(input("Enter monthly investment:\t\t"))
yearly_interest = int(input("Enter yearly interest rate: \t\t"))
number_years = int(input("Enter number of years:\t\t\t"))

monthly_interest = yearly_interest / 100 / 12 + 1
number_months = number_years * 12
future_value = 0

for i in range(number_months):
    
    future_value += monthly_invest
    future_value = future_value * monthly_interest
    
print(f"Future value:\t\t\t\t\t{future_value:.2f}")