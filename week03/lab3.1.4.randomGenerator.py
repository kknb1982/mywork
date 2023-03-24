# Prints out a random number between 1 and 10
# Author: Kirstin Barnett
# Based on code from Andrew Beatty

import random
x = int(input ("What is the lower limit of the range: "))
y = int(input ("What is the upper limit of the range: "))
number = random.randint (x,y)
print (f"Here is a random number between {x} and {y}: {number}.")
