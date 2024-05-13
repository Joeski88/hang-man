import random
from words import words

def print_hangman(wrong):
    if(wrong == 1):
        print("\n+----+")
    elif(wrong == 2):
        print("\n+----+")
        print("       |")
        print("       |")
        print("       |")
    elif(wrong == 3):
        print("\n+----+")
        print("       |")
        print("       |")
        print("       |")
        print("  ======")
    elif(wrong == 4):
        print("\n+----+")
        print("  O    |")
        print("       |")
        print("       |")
        print("  ======")
    elif(wrong == 5):
        print("\n+----+")
        print("  O    |")
        print("  |    |")
        print("       |")
        print("  ======")
    elif(wrong == 6):
        print("\n+----+")
        print("  O    |")
        print(" /|    |")
        print("       |")
        print("  ======")
    elif(wrong == 7):
        print("\n+----+")
        print("  O    |")
        print(" /|\   |")
        print("       |")
        print("  ======")
    elif(wrong == 8):
        print("\n+----+")
        print("  O    |")
        print(" /|\   |")
        print(" /     |")
        print("  ======")
    elif(wrong == 9):
        print("\n+----+")
        print("  O    |")
        print(" /|\   |")
        print(" / \   |")
        print("  ======")




print("Welcome to Hangman")
print("------------------------------------")

### Start menu for user
choice = ""

while True:
    print("1) Play Game")
    print("2) Rules")
    print("3) Exit Game")

    choice = input("Menu Select: ")

    choice = choice.strip()
    if (choice == "1"):
            print("Let's Playyyyyyy!!!")
            run()
    elif (choice == "2"):
            print("1. A word is generated at random.\n2. Select desired letters. \n3. Keep guessing letters until you either guess the word or the hangman hangs!!!  \n------------------------------------------------------")
    elif(choice == "3"):
            break
    else:
        print("Invalid Choice, Please Try Again.")