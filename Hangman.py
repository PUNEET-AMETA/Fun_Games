# -*- coding: utf-8 -*-
"""


@author: ameta
"""

import random


words = ["python", "programming", "developer", "hangman", "code"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")
print("You have 6 attempts to guess the word.")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess:", " ".join(guessed))
    else:
        attempts -= 1
        print(f"Incorrect guess. You have {attempts} attempts left.")

if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("You ran out of attempts. The word was:", word)
