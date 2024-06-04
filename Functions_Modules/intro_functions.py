# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:54:21 2024

@author: Arun.Rameshbabu
"""

"""
Functions

Syntax
def function_name([arguments]):
    statements
    [return result]

"""

def print_welcome(message):
    print(message)
    print("This class is cool\n")

 

# More examples
def miles_per_gallon(miles_driven, gallons):
    """
    This function takes in miles driven and gallons of fuel used to retun mpg

    Parameters
    ----------
    miles_driven : int / float
        Number of miles driven.
    gallons : int / float
        Gallons of gas used.

    Returns
    -------
    mpg : float
        Miles per gallon (mpg).

    """
    mpg = miles_driven/gallons
    return mpg



"""
Write the function to calculate the sales tax for the province of NL
Given function arguments:  
    sales_total
    tax_rate
returns
    tax_amount
"""
def sales_tax(sales_total, tax_rate):
    """
    Calculates the tax amount for a given sales total and tax rate

    Parameters
    ----------
    sales_total : int / float
        The total sales amount.
    tax_rate : int / float
        The tax rate in percent (Example 18.5 for 18.5%)

    Returns
    -------
    tax_amount : float
        The tax amount for the given input.

    """
    tax_amount = sales_total * (tax_rate/100)
    return tax_amount



"""
Write the function to calculate the perimeter [and the area] of a rectangle
Given:
    side_a
    side_b
returns
    perimeter
"""
def perimeter(side_a, side_b):
    """
    Takes in the magnitudes of the sides of a rectangle and returns the perimeter

    Parameters
    ----------
    side_a : int / float
        Magnitude of side_a.
    side_b : int / float
        Magnitude of side_b.

    Returns
    -------
    peri : float / int
        Perimeter of a rectangle for the given magnitudes.

    """
    peri = (2 * side_a) + (2 * side_b)
    return peri

perimeter(5, 15)

def main():
    # display a welcome message
    print("Welcome to the functions example")
    # Calling the function
    print_welcome("This message was passed dynamically")
    print_welcome("More such examples")   
    
    example = miles_per_gallon(100, 10)

    miles_per_gallon(500, 14)
    miles_per_gallon(miles_driven=500, gallons=14)

    var1=500
    var2=14
    miles_per_gallon(var1, var2)
    miles_per_gallon(miles_driven=var1, gallons=var2)
    
    sales_tax(100, 10)
    sales_tax(200, 20)

main()