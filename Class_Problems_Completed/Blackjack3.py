# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:23:37 2024

@author: Austin
"""
import random


def blackjack():
    
    choice = random.randint(1, 100)
    
    if choice >= 0 and choice <= 5:
        hand = 'blackjack'
        
    elif choice >= 6 and choice <=  43:
        hand = 'win'
    
    elif choice >= 44 and choice <= 53:
        hand = 'push'
        
    elif choice >= 54 and choice <= 100:
        hand = 'loss'
    
    return hand




def main():
   
    print("BLACKJACK!\nBlackjack payout is 3:2\nEnter 'x' for bet to exit\n")

    starting_money = int(input("Starting money: "))
   
    while starting_money > 0:
        
        bet_amnt = input("\nBet amount: ")
          
        if bet_amnt.lower() == 'x':
            break
        
        elif int(bet_amnt) > starting_money:
            print("You do not have enough money for this bet.")
        
        else:
                    
            blackjack_hand = blackjack()
         
            if blackjack_hand == 'blackjack':
                starting_money = starting_money + (int(bet_amnt) * 1.5)
                print("Blackjack!")
                print(f"Money: {starting_money:.1f}")
                
            elif blackjack_hand == 'win':
                starting_money = starting_money +int(bet_amnt)
                print("You win!")
                print(f"Money: {starting_money:.1f}")
        
            elif blackjack_hand == 'push': 
                print("Push!")
                print(f"Money: {starting_money:.1f}")
               
            elif blackjack_hand == 'loss':
                starting_money = starting_money - int(bet_amnt)
                print("You lose!")
                print(f"Money: {starting_money:.1f}") 
     
    print("Bye!")
    
if __name__ == '__main__':
    main()