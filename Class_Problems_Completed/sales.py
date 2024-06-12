# -*- coding: utf-8 -*-
"""
This module contains functions for gettings sales data from a users.
"""

def get_amount() -> float:
    """
    Gets a sales amount from the user converts it to a float value, and 
    returns the float value
    """
    amount = float(input("Enter amount: "))
    return amount

def get_day() -> int:
    """
    Get a day from the user, converts it to an int value, and returns the 
    int value.
    """
    while True:
        
        day = int(input("Enter day: "))
        if day <= 31:
            return day
            break
        
        else:
            print("Not a valid day")
        
        
def get_month() -> int:
    """
    Gets a month from the user, converts it to an int value, and returns
    the in value.
    """
        
    while True:
        
        month = int(input("Enter month: "))
        if month <= 12:
            return month
            break
        
        else:
            print("Not a valid month")
        
def get_year() -> int:
    """
    Gets a year from the user, converts it to an int value, and returns
    the int value.
    """
    year = int(input("Enter year: "))
    
    return year
    
        
        