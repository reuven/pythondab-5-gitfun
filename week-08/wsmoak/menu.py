#!/usr/bin/env python
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
    choices = sys.argv[1:]
    if choices:
        user_choice = menu(sys.argv[1:])
        print(f"The user chose {user_choice}.")
    else:
        print("Error: You must supply some choices for the menu.")
        print("Usage: ./menu.py foo bar baz")
