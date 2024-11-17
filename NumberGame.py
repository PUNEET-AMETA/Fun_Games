# -*- coding: utf-8 -*-
"""


@author: ameta
"""

import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number:", number)
            break
    except ValueError:
        print("Please enter a valid number.")
