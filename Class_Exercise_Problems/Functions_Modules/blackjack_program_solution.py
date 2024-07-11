# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:57:10 2024

@author: Arun.Rameshbabu
"""

import random

"""
Algorithm
number 95 - 100 -> Blackjack
number 58 - 94 -> Win
number 49 - 57 -> Push
number < 49 -> Lose
"""
def menu():
    """
    Prints menu

    Returns
    -------
    None.

    """
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit")


def bwpl():
    """
    Logic to determine blackjack, win, push or lose

    Returns
    -------
    str
        State of the play.

    """
    num = random.randint(1, 100)
    if num > 95:
        return 'b'
    elif num > 58:
        return 'w'
    elif num > 49:
        return 'p'
    else:
        return 'l'


def main():
    """
    Tha main function for the blackjack game

    Returns
    -------
    None.

    """
    starting_money = float(input("Starting money: "))
    while starting_money > 0:
        bet_amount = input("\nBet amount: ")
        if bet_amount == 'x':
            break
        else:
            bet_amount = int(bet_amount)
            game_state = bwpl()
            if game_state == 'b':
                print("You got a blackjack!")
                starting_money += 1.5 * bet_amount
            elif game_state == 'w':
                print("You won.")
                starting_money += bet_amount
            elif game_state == 'p':
                print("You pushed.")
            else:
                print("You lost.")
                starting_money -= bet_amount
            print(f"Money: {starting_money}")
    print("Bye!")

if __name__ == "__main__":
    menu()
    main()
