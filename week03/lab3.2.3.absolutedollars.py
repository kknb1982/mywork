# Returns the abolute amount of money input in cents
# Author = Kirstin Barnett

money = float(input("Input the amount of money in dollars and cents: "))
absolute_money_in_cents = int(abs(money * 100))
print (f"That amount of money in cent is {absolute_money_in_cents}.")
