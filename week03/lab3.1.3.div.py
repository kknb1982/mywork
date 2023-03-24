# Divides one number by another and gives the integer and remainder
# Author = Kirstin Barnett
# Based on code from Andrew Beatty

x = int(input("Enter the first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x/y)
remainder = x%y

print (f"{x} divided by {y} is {answer} with remainder {remainder}.")
