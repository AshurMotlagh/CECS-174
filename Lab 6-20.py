user = input('Enter a sequence of comma-separated numbers: ')
user_list = user.split(',')
output = ''

for i in range(len(user_list)):
    if user_list[i].isdigit() and int(user_list[i]) % 2:
        output += user_list[i] + ','
print(output[:-1])
