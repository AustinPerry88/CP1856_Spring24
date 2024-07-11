# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:06:42 2024

@author: Austin
"""

print("The Test Scores Program\n")

print("Enter 3 test scores")

print("======================")

score_1 = int(input("Enter test score: "))
score_2 = int(input("Enter test score: "))
score_3 = int(input("Enter test score: "))

print("======================")

total_score = score_1 + score_2 + score_3

print(f"Total Score:   {total_score}")

average_score =  int((score_1 + score_2 + score_3) / 3)

print(f"Average Score: {average_score}")

print("\nBye!")



