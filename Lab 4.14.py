input_string = input("Enter a string consisting of alphabetic characters with \"$\":\n")

while input_string[-1] == '$':
    input_string = input_string[:-1]
    if len(input_string) == 0:
        break

print(input_string)
