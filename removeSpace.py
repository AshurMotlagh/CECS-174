user = input("Enter a string: ")
user = user[::-1]
print("The new string: ", end='')
for character in user:
    if character == ' ':
        continue
    else:
        print(character, end='')