# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:22:45 2024

@author: Austin
"""

total_sales = 0
counter = 0


print("SALES DATA IMPORTER\n")


while True:
    
    if counter == 0:
        print("Enter sales data\n")
        
    else:
        choice = input("Enter more sales data? (y/n): ")
        if choice.lower() == 'y':
            print()
            continue
        else:
            break
    
        
    amount = float(input("Amount:\t\t\t\t"))
    year = int(input("Year: \t\t\t\t"))
    month = int(input("Month (1-12): \t\t"))
    day = int(input("Day (1-31): \t\t\t"))
    
    if month >= 1 and month <= 3:        
        total_sales += amount
        counter += 1
        print(f"\n1.\t\t\t\t\t{year}-{month}-{day}\tQuarter 1\t${amount:.1f}\n")
    
    elif month >= 4 and month <= 6:
        total_sales += amount
        counter += 1
        print(f"\n1.\t\t\t\t\t{year}-{month}-{day}\tQuarter 2\t${amount:.1f}\n")
    
    elif month >= 7 and month <= 9:
        total_sales += amount
        counter += 1
        print(f"\n1.\t\t\t\t\t{year}-{month}-{day}\tQuarter 3\t${amount:.1f}\n")
    
    elif month >= 10 and month <= 12:
        total_sales += amount
        counter += 1
        print(f"\n1.\t\t\t\t\t{year}-{month}-{day}\tQuarter 4\t${amount:.1f}\n")
        
print("\nTotal Sales")
print("-" * 20)
print(f"${total_sales:.1f}")
print("\nBye!")
    