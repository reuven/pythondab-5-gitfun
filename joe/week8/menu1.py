#!/usr/bin/env ipython

# (1) Write a module, "menu.py", in which you define a single function,  "menu".
# This function should take any number of string arguments,  which are then presented
# to the user.

# If the user chooses one of the arguments (as a string), then that  string is
# returned from the function.  If not, then the user is  given another chance to
# enter a choice.

# For example:

#         import menu
#         user_choice = menu.menu('a', 'b', 'c')

import sys


def menu(*args):
    return args


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # print(sys.argv)
        print(menu(sys.argv[1]))
    else:
        print(menu("a"))
