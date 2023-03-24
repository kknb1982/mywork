# reads in a percentage and outputs the corresponding grade
# Author: Kirstin Barnett

percentage = float(input("please enter the percentage: "))

if percentage <0 or percentage >100:
    print("please enter a number between 0 and 100")

elif percentage  < 40:
    print(f"The score of {percentage} is a: fail")
elif percentage < 50:
    print(f"The score of {percentage} is a: pass")
elif percentage < 60:
    print(f"The score of {percentage} is a: merit 2")
elif percentage < 70:
    print (f"The score of {percentage} is a: merit 1")
else:
    print(f"The score of {percentage} is a: distinction")