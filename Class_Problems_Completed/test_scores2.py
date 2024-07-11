# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:02:57 2024

@author: Austin
"""

print("The Test Scores program\n")
print("Enter 999 to end input")
print("=======================")



test_score = 0
total_score = 0
temp_score = 0
num_tests = 0

while temp_score != 999:
    temp_score = int(input("Enter test score:\t"))    
    if temp_score >=0 and temp_score <= 100:
        test_score += temp_score
        num_tests += 1
    elif temp_score != 999:
        print("Test score must be from 0 through 100. Try again.")
         
  
if num_tests > 0:        
    average_score = test_score / num_tests
    print("=======================")
    print(f"Total score: {test_score:.0f}")
    print(f"Average score: {average_score:.0f}")

print("\nBye!")
    
    



        
         

    