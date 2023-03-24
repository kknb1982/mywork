# Imports 10 random numbers, selects each number in turn and prints out the remaining numbers in the queue.
# Based on code from Andrew Beatty
# Author: Kirstin Barnett

import random
queue = []
number_of_numbers = 10
range_to = 100

for n in range (0, number_of_numbers):
    queue.append(random.randint(0,range_to))
    print (f"queue is {queue}")

while len(queue) != 0:
    current_number = queue.pop(0)
    print(f"The current number is {current_number} and the queue is {queue}")

print ("the queue is now empty")