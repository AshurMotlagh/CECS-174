def updateList(input_list, input_str):
    input_list[1] = input_str
    input_list[2] = input_str
    input_list[3] = input_str
    return input_list

def main():
    list = []
    print("This program requires a list with a minimum of 4 items.")
    while True:
        user_input = input("Enter the item of the list, or 'Q' to quit:")
        if 'q' in user_input.lower():
            break
        else:
            list.append(user_input)
    if len(list) < 4:
                print("Not enough items in the list - goodbye.")
    else:
                compare = input("Enter a string:")
                print(updateList(list, compare))

main()
