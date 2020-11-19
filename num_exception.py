total = 0
while True:
    try:
        user = float(input("Enter a number, or 2 non-numbers to quit:"))
        total = total + float(user)
    except ValueError:
        try:
            user = input("Enter a number, or another non-number to quit:")
            total = total + float(user)
        except ValueError:
            break

print("The total is", total)