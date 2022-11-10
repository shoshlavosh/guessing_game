"""A number-guessing game."""

import random
answer = random.randint(1, 101)
guesses = 0
name = input("What's your name? > ")
print(f"Hi, {name}! Let's play a guessing game")

guess = ""
while answer != guess:
    guess = input(f"Choose a number between 1 and 100 >")

    if guess is not guess.isnumeric():
        print("Try again! Guess is not a valid number.")
        guess = input("Please choose a number between 1 and 100. > ")
    
    if int(guess) > 100:
        guess = input("Please choose a number between 1 and 100. >")
    
    if int(guess) < 1:
        guess = input("Please choose a number between 1 and 100. > ")

    guesses += 1

    if int(guess)<answer:
        print("Guess too low try again")
    if int(guess)>answer:
        print("Guess too high try again")
    if int(guess)==answer:
        print("correct answer!")
        print(f"You guessed it in {guesses} tries")
        break
        


