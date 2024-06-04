# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:58:16 2024

@author: Arun.Rameshbabu
"""

def future_value_calc(monthly_investment, interest_rate, years):
    future_value = 0
    interest_rate_monthly = (interest_rate/12)/100
    num_months = years * 12
    
    # Loop through
    for mnth in range(int(num_months)):
        future_value += monthly_investment # Add new investment
        interest_for_mnth = future_value * interest_rate_monthly # Calculate interest for month
        future_value += interest_for_mnth # Add interest to the principal
    
    return future_value

def main():
    while True:
        monthly_invest = float(input("Enter monthly investment:\t\t"))
        intrest_rate_yr = float(input("Enter yearly interest rate:\t\t"))
        num_years = float(input("Enter the number of years:\t\t"))
        
        fut_value = future_value_calc(monthly_invest, intrest_rate_yr, num_years)
        print(f"Future Value:\t\t\t\t\t{fut_value:.2f}")
        
        choice = input("Continue (y/n)?: ")
        if choice.lower() != 'y':
            break
    print("\nBye!")

main()