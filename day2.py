print("welcome to the tip calculator")
price=int(input("what was the total bill price?"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill?"))
calc=price*(1+tip/100)/people
print(f"each person should pay: {str(round(calc, 2))}")
