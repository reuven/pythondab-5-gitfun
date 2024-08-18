# menu.py

import sys

def menu(*options):
    while True:
        print("Please choose one of the following options:")
        for option in options:
            print(f"- {option}")
        
        choice = input("Enter your choice: ").strip()
        
        if choice in options:
            return choice
        else:
            print(f"Invalid choice. Please select from: {', '.join(options)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_choice = menu(*sys.argv[1:])
        print(f"You chose: {user_choice}")
    else:
        print("No options provided. Please run the script with options.")

