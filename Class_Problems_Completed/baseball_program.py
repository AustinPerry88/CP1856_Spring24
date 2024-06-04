# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:14:33 2024

@author: Austin
"""

def separator():
    print("=" * 60)
    
def title():
    print("\t\t\t\t\tBaseball Team Manager")
    
def menu():
    print("Menu Options")
    print("1 - Calculate batting average")
    print("2 - Exit program")
    
def batting_average(bats, hits):
    average = hits / bats
    return average

def main():
     
    separator()
    title()
    menu()
    separator()
        
    while True:
           
        menu_option = input("\nMenu option: ")
        if menu_option == '2':
            print("Bye!")
            break
        elif menu_option == '1':
            print("Calculate batting average...")
            number_bats = int(input("Official number of at bats: "))
            number_hits = int(input("Number of hits: "))
            average = batting_average(number_bats, number_hits)        
            print(f"Batting average: {average:.3f}")
        else:
            print("Not a valid option. Please try again.\n")
            menu()
    
        
if __name__ == '__main__':
    main()