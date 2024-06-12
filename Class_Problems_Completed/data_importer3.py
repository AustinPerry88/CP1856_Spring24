# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:18:42 2024

@author: Austin
"""
import sales
help(sales)

total_sales = 0
counter = 0

def sales_data():
    global total_sales, counter
    
    
    amount = sales.get_amount()
    year = sales.get_year()
    month = sales.get_month()
    day = sales.get_day()
    
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


def main():
    
    global total_sales, counter
    
    print("SALES DATA IMPORTER\n")
    
    while True:
        
        if counter == 0:
            print("Enter sales data\n")
            sales_data()
            
        else:
            choice = input("Enter more sales data? (y/n): ")
            if choice.lower() == 'y':
                sales_data()
                
            
            elif choice.lower() == 'n':
                break
            
            else:
                print("Not a valid option!")
     
            
    print("\nTotal Sales")
    print("-" * 20)
    print(f"${total_sales:.1f}")
    print("\nBye!")
    
if __name__ == '__main__':
    main()