while True:
    tim1 = input('Enter the first time as hours:minutes in 24 hour format:\n')
    tim2 = input('Enter the second time as hours:minutes in 24 hour format:\n')

    time1 = tim1.split(':')
    time2 = tim2.split(':')


    if ':' not in tim1 or ':' not in tim2:
        print("Invalid format !!!")
        continue

    elif not time1[0].isdigit() or not time1[1].isdigit() or not time2[1].isdigit() or not time2[0].isdigit():
        print("Invalid entry - input should be numbers only.")
        continue

    elif int(time1[0]) >= 24 or int(time2[0]) >= 24 or int(time1[1]) >= 59 or int(time2[1]) >= 59:
        print('Invalid time range.')
        continue

    else:
        if int(time1[0]) < int(time2[0]):
            print("time1 comes first")

        elif int(time1[0]) == int(time2[0]):
            if int(time1[1]) < int(time2[1]):
                print("time1 comes first")

            elif int(time1[1]) == int(time2[1]):
                print("time1 and time2 are the same")

            else:
                print("time2 comes first")

        else:
            print("time2 comes first")

    flag = input("Would you like to try again, 'Yes' for continue, quit otherwise: ").upper()
    if flag[0] == 'Y':
        continue
    else:
        break
print("Goodbye")