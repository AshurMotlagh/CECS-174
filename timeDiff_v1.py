tim1 = input('Enter the first time as hours:minutes in 24 hour format:\n')
tim2 = input('Enter the second time as hours:minutes in 24 hour format:\n')

time1 = tim1.split(':')
time2 = tim2.split(':')

if time1[0] < time2[0]:
    print("time1 comes first")
elif time1[0] == time2[0]:
    if time1[1] < time2[1]:
        print("time1 comes first")
    elif time1[1] == time2[1]:
        print("time1 and time2 are the same")
    else:
        print("time2 comes first")
else:
    print("time2 comes first")
