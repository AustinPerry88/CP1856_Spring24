# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:53:32 2024

@author: Austin
"""

print("SALES DATA IMPORTER")

print("\nEnter sales data\n")


amount = float(input("Amount:\t\t\t\t"))
year = int(input("Year: \t\t\t\t"))
month = int(input("Month (1-12): \t\t"))
day = int(input("Day (1-31): \t\t\t"))

total_sales = amount

print(f"\n1.\t\t\t\t\t{year}-{month}-{day}\t\t\t${amount:.1f}\n")

amount = float(input("Amount:\t\t\t\t"))
year = int(input("Year: \t\t\t\t"))
month = int(input("Month (1-12): \t\t"))
day = int(input("Day (1-31): \t\t\t"))

total_sales = total_sales + amount

print(f"\n1.\t\t\t\t\t{year}-{month}-{day}\t\t\t${amount:.1f}\n")

amount = float(input("Amount:\t\t\t\t"))
year = int(input("Year: \t\t\t\t"))
month = int(input("Month (1-12): \t\t"))
day = int(input("Day (1-31): \t\t\t"))

total_sales = total_sales + amount

print(f"\n1.\t\t\t\t\t{year}-{month}-{day}\t\t\t${amount:.1f}\n")

print("Total Sales")
print("----------")
print(f"${total_sales:.1f}")

print("\nBye!")
