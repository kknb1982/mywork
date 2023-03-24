# Prompts a user to guess a number until it matches.  
# Helps the user by letting them know if the guess if too high to too low
# Author: Kirstin Barnett
# Based on code by Andrew Beatty

import random
number_to_guess = random.randint(1,100)

guess = int(input("Please guess the number, it is between 1 and 100: "))
while guess != number_to_guess:
    if guess <number_to_guess:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Please guess again: "))

print(f"Well done! Yes the number was {number_to_guess}.")