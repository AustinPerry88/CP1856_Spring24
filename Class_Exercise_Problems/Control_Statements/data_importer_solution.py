# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:35:17 2024

@author: Arun.Rameshbabu
"""

"""
Algorithm

print statement\n
print statement\n

total_sales = 0
counter = 1
choice = 'y'

while choice == 'y':
    amount <- int(input)
    year <- int(input)
    month <- int(input)
    day <- int(input)
    
    if month == 1 or month == 2 or month == 3:
        quarter = 'Quarter 1'
    elif month == 4 or month == 5 or month == 6:
        quarter = 'Quarter 2'
    elif month == 7 or month == 8 or month == 9:
        quarter = 'Quarter 3'
    elif month == 10 or month == 11 or month == 12:
        quarter = 'Quarter 4'
    else:
        print ("Wrong input entered, try again")
        continue
    
    print \n{counter}.\t\t{year}-{month}-{day}\t\t{quarter}\t\t${amount:.1f}
    total_sales += amount
    counter += 1
    choice = input("Enter more sales? (y/n): ")

print("Total Sales:")
print('-'*16)
print(f"${total_sales}\n")
print("Bye!")
"""

print("SALES DATA IMPORTER\n")
print("Enter sales data")

total_sales = 0
counter = 1
choice = 'y'

while choice == 'y':
    amount = int(input("\nAmount:\t\t\t"))
    year = int(input("Year:\t\t\t"))
    month = int(input("Month (1-12):\t"))
    day = int(input("Day (1-31):\t\t"))
    
    if (month == 1) or (month == 2) or (month == 3):
        quarter = 'Quarter 1'
    elif (month == 4) or (month == 5) or (month == 6):
        quarter = 'Quarter 2'
    elif (month == 7) or (month == 8) or (month == 9):
        quarter = 'Quarter 3'
    elif (month == 10) or (month == 11) or (month == 12):
        quarter = 'Quarter 4'
    else:
        print ("Wrong input entered, try again")
        continue
    
    # Optional Check
    if (day < 1) or (day > 31):
        print ("Wrong input entered, try again")
        continue
    
    print (f"\n{counter}.\t\t\t\t{year}-{month}-{day}\t\t{quarter}\t\t${amount:.1f}")
    total_sales += amount
    counter += 1
    choice = input("\nEnter more sales? (y/n): ")

print("\nTotal Sales:")
print('-'*16)
print(f"${total_sales:.1f}\n")
print("Bye!")
