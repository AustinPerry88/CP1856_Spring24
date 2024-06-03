# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:54:22 2024

@author: Austin
"""



def to_celsius(temp):
    """
    Converts temperature in fahrenheit to celsius

    Parameters
    ----------
    temp : float
        Temperature in fahrenheit

    Returns
    -------
    fahrenheit : float
        Temperature in celsius

    """
    celsius = (temp * (9/5)) + 32
    
    return celsius

def to_fahrenheit(temp):
    """
    

    Parameters
    ----------
    temp : float
        temperature in fahrenheit

    Returns
    -------
    celsius : float
        temperature in fahrenheit

    """
    fahrenheit = (temp - 32) * (5/9)
    
    return fahrenheit
    
    