# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:52:09 2024

@author: Arun.Rameshbabu
"""

"""
Algorithm

print statements 
print
print \n

starting_money <- int(input)
print()

while (starting_money > 0):
    bet_amount <- input
    if bet_amount == 'x':
        break
    else:
        game_state = input(b/w/p/l)
        if game_state == 'b':
            starting money += bet_amount * 1.5
            print(f'Money:{starting_money}\n')
        elif game_state == 'w':
            starting money += bet_amount
            print(f'Money:{starting_money}\n')
        elif game_state == 'p':
            print(f'Money:{starting_money}\n')
            continue                     # Skips to the next iteration in the loop
        elif game_state == 'l':
            starting money -= bet_amount
            print(f'Money:{starting_money}\n')

print("Bye!")
"""

print("BLACKJACK!")
print("Blackjack payout ratio is 3:2")
print("Enter 'x' for bet to exit\n")

starting_money = int(input("Starting money: "))
print()

while starting_money > 0:
    bet_amount = input("Bet amount: ")
    if (bet_amount == 'x') or (int(bet_amount) > starting_money):
        break
    else:
        bwpl = input("Blackjack, Win, Push or Lose?(b,w,p,l): ").lower()
        if bwpl == 'b':
            starting_money += (int(bet_amount) * 1.5)
            print(f'Money: {starting_money}\n')
        elif bwpl == 'w':
            starting_money += int(bet_amount)
            print(f'Money: {starting_money}\n')
        elif bwpl == 'p':
            print(f'Money: {starting_money}\n')
            continue
        elif bwpl == 'l':
            starting_money -= int(bet_amount)
            print(f'Money:{starting_money}\n')
        else:
            print("Invalid input")

print("Bye!")

