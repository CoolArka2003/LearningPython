print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
people=int(input("How many people to split the bill? "))
percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip=((percentage/100)*bill)/people+bill/people
tip=str(round(tip,2))
print("Each person should pay: $"+tip)