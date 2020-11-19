income = int(input("Enter the income:\n"))

if income <= 50000:
    tax = income * .01

elif income <= 75000:
    tax = 500 + (income - 50000)*.02

elif income <= 100000:
    tax = 1000 + (income - 75000) * .03

elif income <= 250000:
    tax = 1750 + (income - 100000) * .04

else:
    tax = 2750 + (income - 250000) * .05

print('The tax payable would be $', tax)
