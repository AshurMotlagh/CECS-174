# Define the price of a stamp in pennies.
FIRST_CLASS_STAMP_PRICE = 44
dollars = float(input("Enter number of dollars:"))
dollars = dollars * 100

# Compute and print the number of stamps to dispense.
stamps = dollars // FIRST_CLASS_STAMP_PRICE
print("First class stamps", int(stamps))

# Compute the number of quarters, dimes, nickels and pennies to return
mod = int(dollars) % FIRST_CLASS_STAMP_PRICE
quarter = mod // 25
mod = mod - (25*quarter)  # mod = mod % 25
dime = mod // 10
mod = mod - (10*dime)  # mod = mod % 10
nick = mod // 5
mod = mod - (5*nick)  # mod = mod % 5
pen = mod // 1

print("Your change is:\n", quarter, 'quarters\n', dime, 'dimes\n', nick, 'nickels\n', pen, 'pennies')
