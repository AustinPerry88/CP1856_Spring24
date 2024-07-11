# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:59:56 2024

@author: Austin
"""

import temp_module

print("MENU\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit")




while True:

    choice = input("\nEnter menu option: ")
    
    if choice == '1':
       temp = float(input("Enter degrees Fahrenheit: "))
       conversion = temp_module.to_fahrenheit(temp)
       print(f"Degrees Celsius: {conversion:.1f}")
          
    elif choice == '2':
        temp = float(input("Enter degrees Celsius: "))
        conversion = temp_module.to_celsius(temp)
        print(f"Degrees Fahrenheit: {conversion:.1f}")
        
    convert_again = input("\nConvert another temperature? (y/n): ")
    
    if convert_again.lower() == 'n':
        break

        
             
         
