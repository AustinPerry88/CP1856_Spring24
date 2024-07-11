# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:38:08 2024

@author: Arun.Rameshbabu
"""

def seprator_line(seperator):
    """
    Prints the seperator line

    Parameters
    ----------
    seperator : char
        Character that will be printed 65 times.

    Returns
    -------
    None.

    """
    print(65*seperator)


def display_title(title):
    """
    Prints the tile as specified

    Parameters
    ----------
    title : str
        Title to be printed.

    Returns
    -------
    None.

    """
    print(f'\t\t\t\t\t{title}')


def menu():
    """
    Prints the menu

    Returns
    -------
    None.

    """
    print('MENU OPTIONS:')
    print('1 - Calculate Batting Average')
    print('2 - Exit Program')


def batting_average(at_bats, hits):
    """
    Calculates and returns batting average

    Parameters
    ----------
    at_bats : int
        Number of at_bats.
    hits : int
        Number of hits.

    Returns
    -------
    float
        Returns batting average.

    """
    return hits/at_bats


def main():
    while True:
        menu_option = input("Menu option: ")
        if menu_option == '1':
            print("Calculating batting average...")
            off_at_bats = int(input("Official Number of at bats: "))
            off_hits = int(input("Number of hits: "))
            bat_avg = batting_average(off_at_bats, off_hits)
            print(f"Batting average: {bat_avg:.3f}\n")
        elif menu_option == '2':
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            menu()
            print()


if __name__ == '__main__':
    seprator_line('=')
    display_title('Baseball Team Manager')
    menu()
    seprator_line('=')
    main()
    