name = []
amount = []
# count = -1
while True:
    name_input = input("What is the name of the customer? ")

    if '' == name_input:
        break

    amount_input = str(input("What is the purchase amount (numbers only)? "))

    while not amount_input.isdigit():
        amount_input = input("What is the purchase amount (numbers only)? ")
        if amount_input.isdigit():
            break

    if name_input not in name:
        name.append(name_input)
        amount.append(int(amount_input))
        # count += 1

    elif name_input in name:
        repeat = name.index(name_input)
        amount[repeat] += int(amount_input)
        # amount[count] += int(amount_input)

max_amount = max(amount)
index = amount.index(max_amount)
top_cus = name[index]
print(top_cus, 'spent', '$', max_amount)


