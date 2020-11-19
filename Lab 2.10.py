food = (float(input("Enter the charge for food: ")))
tax = .07 * food
tip = .18 * food
total = tax + tip + food
print("Tax: $", format(tax,'.2f'),",", "Tip: $", format(tip, '.2f'), ",", "Total: $", format(total,'.2f'))