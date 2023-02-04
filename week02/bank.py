# A program that adds two user entered amounts and prints them in a readable format
# Author: Kirstin Barnett

amount1 = input("Enter the first amount in cents: ")
amount2 = input ("Enter the second amount in cents: ")
sum = int(amount1) + int(amount2)
total = int(sum)/100
print (f"The sum of these is €{total}")

