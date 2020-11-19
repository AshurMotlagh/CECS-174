price_chart = [[10, 10, 10, 10, 10],
               [20, 20, 20, 10, 10],
               [20, 20, 20, 10, 10],
               [20, 20, 20, 10, 10],
               [40, 30, 30, 20, 20]]

while True:
    condition = input("Pick a (S)eat, a (P)rice or (Q)uit:").lower()
    if condition == 's':
        row = int(input("Enter the row: ")) - 1
        column = int(input("Enter the column: ")) - 1
        if price_chart[row][column] != 0:
            print("Sold, for $", price_chart[row][column], '!')
            price_chart[row][column] = 0
        else:
            print("Sorry, that seat is not available.")
        continue

    elif condition == 'p':
        valid_seat = 0
        price = int(input("How much do you want to spend?"))
        for i in price_chart:

            if price in i:
                seat = price_chart.index(i)
                print("You can have seat", seat + 1, i.index(price) + 1)
                price_chart[seat][i.index(price)] = 0
                break

            else:
                valid_seat += 1

            # else:
            #     print("Sorry, no tickets avaliable at that price.")
            #     break


            # elif i not in price_chart:
            #     valid_seat += 1

        if valid_seat == 5:
            print("Sorry, no tickets available at that price.")
            # elif i not in price_chart:
            #     print("Sorry, no tickets avaliable at that price.")
            #     continue

    elif condition == 'q':
        for rows in price_chart:
            for col in rows:
                print(col, end=' ')
            print()
        break

    elif condition != 's' or condition != 'p' or condition != 'q':
        print("That wasn't a valid option.")

    # else:
    #     print("That wasn't a valid option.")

