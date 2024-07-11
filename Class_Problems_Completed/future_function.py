# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:44:45 2024

@author: Austin
"""

def future_calculator(monthly_invest, yearly_interest, number_years):

    monthly_interest = yearly_interest / 100 / 12 + 1
    number_months = number_years * 12
    future_value = 0
    
    for i in range(number_months):
        
        future_value += monthly_invest
        future_value = future_value * monthly_interest
    
    return future_value

def main():
    
    print("Welcome to the Future Value Calculator\n")
    
    while True:
    
        monthly_invest = int(input("Enter monthly investment:\t\t"))
        yearly_interest = int(input("Enter yearly interest rate: \t\t"))
        number_years = int(input("Enter number of years:\t\t\t"))
        
        future_value = future_calculator(monthly_invest, yearly_interest, number_years)
        
        print(f"Future value:\t\t\t\t\t{future_value:.2f}")
    
        choice = input("Continue (y/n)?  ")
        if choice.lower() != 'y':
            break
        
main()