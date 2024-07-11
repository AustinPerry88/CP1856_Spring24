# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:39:57 2024

@author: Austin
"""

print("="*100)
print("\t\t\t\t\t\t\tBaseball Team Manager")
print("MENU OPTIONS")
print("1 - Calculate batting average\n2 - Exit program")
print("="*100)


while True:
    
    choice = int(input("Menu option: "))
    
    if choice == 1:
        print("Calculating batting average...")
        at_bats = int(input("Official number of at bats: "))
        num_hits = int(input("Number of hits: "))
        print(f"Batting average:{num_hits/at_bats:.3f}\n")
              
    elif choice == 2:
        print("Bye!")
        break
    
    
    else:
        print("Not a valid option. Please try again.\n")
                  