num_list = []
while len(num_list) < 5:
    num = float(input("Please enter a floating point number:"))
    if num not in num_list:
        num_list.append(num)
    else:
        print("The number is already in the list!")

print("The numbers are:", num_list)
