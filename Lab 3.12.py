user_response = int(input("Enter a positive integer between 1 and 7: "))
week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
if user_response <= 0 or user_response > 7:
    print("ERROR")
else:
    print(week[user_response - 1])


'''
if user_response == 1:
    print(week[0])

elif user_response == 2:1
    print(week[1])

elif user_response == 3:
    print(week[2])

elif user_response == 4:
    print(week[3])

elif user_response == 5:
    print(week[4])

elif user_response == 6:
    print(week[5])

elif user_response == 7:
    print(week[6])

else:
    print("ERROR")
'''