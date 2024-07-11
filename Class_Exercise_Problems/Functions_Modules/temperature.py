# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:33:32 2024

This module contains functions for converting 
between degrees Faranheit and degrees Celsius 
"""

def to_celsius(faranheit: float) -> float:
    """
    Accepts degrees Faranheit (faranheit argument)
    Returns degrees Celsius 
    """
    celsius = (faranheit - 32) * (5/9)
    return celsius

def to_faranheit(celsius) -> float:
    """
    Accepts degrees Celsius (celsius argument)
    Returns degrees Faranheit
    """
    faran = (celsius * (9/5)) + 32
    return faran
