user_input = input("Enter a string:")
user_list = user_input.split()
final_list = []

print("Original list is", user_list)

for i in range(len(user_list)):
    if len(user_list[i]) >= 4:
        final_list.append(user_list[i])

print("Final list is", final_list)