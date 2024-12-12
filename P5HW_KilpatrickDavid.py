#David Kilpatrick
#11-21-2024
#P5HW
#Math Quiz Game

import random

def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f" {num1}")
    print(f"+{num2}")
    return correct_answer

def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    print(f" {num1}")
    print(f"-{num2}")
    return correct_answer

def check_answer(correct_answer):
    guesses = 0
    while True:
        answer = int(input("Enter answer: \n"))
        guesses += 1
        
        if answer < correct_answer:
            print("Sorry, guess is too low.\n")
        elif answer > correct_answer:
            print("Sorry, guess is too high.\n")
        else:
            print("Congratulations!!! Your answer is correct.")
            print(f"Number of guesses: {guesses}\n")
            print()
            break

def display_menu():
    print("MAIN MENU")
    print("-----------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")
    print("-----------------------------")

def math_game():
    print("Welcome to Math Quiz\n")
    
    while True:
        display_menu()
        choice = input("Please choose one of the menu options: ")
        
        if choice == "3":
            print("Thank you for playing...")
            print("Bye!!")
            break
        
        elif choice == "1":
            correct_answer = add_numbers()
            check_answer(correct_answer)
            
        elif choice == "2":
            correct_answer = subtract_numbers()
            check_answer(correct_answer)
            
        else:
            print("Invalid Choice, Select 1, 2, or 3")
            continue
math_game()
