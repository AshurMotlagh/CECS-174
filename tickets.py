total = 20
total_people = 0
while total > 0:
    print("There are currently", total, "tickets remaining.")
    user_input = int(input("How many tickets would you like to purchase? \n"))
    while True:
        if user_input > 4 or user_input > total:
            print("Sorry, you can't buy that many.")
            user_input = int(input("How many tickets would you like to purchase? \n"))
            continue
        else:
            total -= user_input
            total_people += 1
            break
print("The total number of buyers was", total_people)
