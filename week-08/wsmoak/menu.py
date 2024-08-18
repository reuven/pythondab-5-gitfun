#!/usr/bin/env python
"""
Usage: menu.py foo bar baz
"""
import sys

def menu(args):
    """Presents a list of choices to the user and asks them to enter a choice.
    If the choice is not in the list, asks again.
    Accepts: a list of strings containing the choices
    Returns: the chosen item as a string
    """
    print("The options are:")
    for arg in args:
        print(arg)

    choice = None
    while not choice in args:
        choice = input("Enter your choice ")

    return choice


if __name__ == '__main__':
    user_choice = menu(sys.argv[1:])
    print(f"The user chose {user_choice}.")