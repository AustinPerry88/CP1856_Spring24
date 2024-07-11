# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:02:47 2024

@author: Austin
"""

print("BLACKJACK!\nBlackjack payout is 3:2\nEnter 'x' for bet to exit\n")

starting_money = int(input("Starting money: "))


while starting_money > 0:
    
    bet_amnt = input("\nBet amount: ")
      
    if bet_amnt.lower() == 'x':
        break
    
    blackjack = input("Blackjack, win, push, or lose? (b/w/p/l): ")
 
    if blackjack.lower() == 'b':
        starting_money = starting_money + (int(bet_amnt) * 1.5)
        print(f"Money: {starting_money:.1f}")
        
    elif blackjack.lower() == 'w':
        starting_money = starting_money +int(bet_amnt)
        print(f"Money: {starting_money:.1f}")

    elif blackjack.lower() == 'p':   
        print(f"Money: {starting_money:.1f}")
       
    elif blackjack.lower() == 'l':
        starting_money = starting_money - int(bet_amnt)
        print(f"Money: {starting_money:.1f}") 
    
    
print("Bye!")