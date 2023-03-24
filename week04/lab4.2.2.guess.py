# Prompts a user to guess a number until it matches
# Author: Kirstin Barnett
# Based on code by Andrew Beatty

number_to_guess = 15

guess = int(input("Please guess the number: "))
while guess != number_to_guess:
    print("Wrong")
    guess = int(input("Please guess again: "))

