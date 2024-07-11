# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:35:38 2024

@author: Arun_Rameshbabu
"""

import temperature

def menu():
    """
    

    Returns
    -------
    None.

    """
    print("MENU")
    print("1. Farenheit to Celsius")
    print("2. Celsius to Faranhet")

def main():
    """
    

    Returns
    -------
    None.

    """
    menu_option = input("\nEnter a menu option: ")
    if menu_option == '1':
        deg_faran = float(input("Enter degrees Faranheit: "))
        deg_cel = temperature.to_celsius(deg_faran)
        print(f"Degrees Celsius: {deg_cel:.1f}")
    elif menu_option == '2':
        deg_cel = float(input("Enter degrees Celsius: "))
        deg_faran = temperature.to_faranheit(deg_cel)
        print(f"Degrees Faranheit: {deg_faran:.1f}")
    else:
        print("Invalid Input. Please try again")

if __name__ == '__main__':
    menu()
    while True:
        main()
        again = input("\nConvert another temperature (y/n): ")
        if again == 'n':
            break

