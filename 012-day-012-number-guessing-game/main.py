import art
import os
import random

os.system("cls||clear")
print(art.logo)

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I`m thinking of a number between 1 and 100. Guess My Number!")
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
    random_number = random.randint(1, 100)
    guess = ""
    # print(random_number)
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    while attempts > 0 and guess != random_number:

        print(f"You have {attempts} attempts remaining to guess my number.")
        guess = int(input("Make a guess: "))

        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
            
        attempts -= 1

    if attempts > 0:
        print(f"Wohoo! You got it! My number was {random_number}")
    else:
        print(f"You've run out of guesses, you loose. My number was {random_number}")

number_guessing_game()