while True:
    print("******** menu ******** \n1 - Addition \n2 - Subtraction \n3 - Multiplication \n4 - Division \n5 - Exit")
    operation = int(input("Please select the operation:\n"))
    if operation <= 4:
        first_num = int(input("Enter the first number:\n "))
        sec_num = int(input("Enter the second number:\n "))
        if operation == 1:
            print("The result is", first_num + sec_num)
            continue
        elif operation == 2:
            print("The result is", first_num - sec_num)
            continue
        elif operation == 3:
            print("The result is", first_num * sec_num)
            continue
        elif operation == 4:
            print("The result is", first_num // sec_num)
            continue
    else:
        break

print("Goodbye")
