def main():
    valid_response = ['and','or', 'nand', 'nor', 'xnor', 'xor', 'not']
    print("Valid Logic gates include:", valid_response)
    gate_choice = input('Pick your logic gate from above: ', ).lower()

    while gate_choice not in valid_response:
        print("Enter Valid Logic Gate! Pick From:", valid_response)
        gate_choice = input('Pick your logic gate: ').lower()
    while gate_choice != 'quit':
        if gate_choice == 'and':
            and_gate()
        elif gate_choice == 'or':
            or_gate()
        elif gate_choice == 'nand':
            nand_gate()
        elif gate_choice == 'nor':
            nor_gate()
        elif gate_choice == 'xor':
            xor_gate()
        elif gate_choice == 'nxor':
            xnor_gate()
        elif gate_choice == 'not':
            not_gate()
        gate_choice = input('Pick your logic gate or press \"enter key\" to quit: ').lower()
        if gate_choice not in valid_response:
            break
        else:
            continue


def xnor_gate():
    value_1 = input("Enter a value for A (1 or 0): ")
    value_2 = input("Enter a value for B (1 or 0): ")
    print("Your inputs A =", value_1, "and B = ", value_2)
    if value_1 == value_2:
        print(True, '\n')
    else:
        print(False, '\n')


def or_gate():
    value_1 = input("Enter a value for A (1 or 0): ")
    value_2 = input("Enter a value for B (1 or 0): ")
    print("Your inputs A =", value_1, "and B = ", value_2)
    if (int(value_2) + int(value_1)) <= 2:
        print(True, '\n')
    else:
        print(False, '\n')


def nand_gate():
    value_1 = int(input("Enter a value for A (1 or 0): "))
    value_2 = int(input("Enter a value for B (1 or 0): "))
    print("Your inputs A =", value_1, "and B = ", value_2)
    if (value_2 * value_1) == 0:
        print(True, '\n')
    else:
        print(False, '\n')


def nor_gate():
    value_1 = int(input("Enter a value for A (1 or 0): "))
    value_2 = int(input("Enter a value for B (1 or 0): "))
    print("Your inputs A =", value_1, "and B = ", value_2)
    if (value_2 * value_1) == 0:
        print(True, '\n')
    else:
        print(False, '\n')


def xor_gate():
    value_1 = int(input("Enter a value for A (1 or 0): "))
    value_2 = int(input("Enter a value for B (1 or 0): "))
    print("Your inputs A =", value_1, "and B = ", value_2)
    if value_1 + value_2 == 1:
        print(True, '\n')
    else:
        print(False, '\n')


def and_gate():
    value_1 = int(input("Enter a value for A (1 or 0): "))
    value_2 = int(input("Enter a value for B (1 or 0): "))
    print("Your inputs A =", value_1, "and B = ", value_2)
    if value_1 * value_2 == 1:
        print(True, '\n')
    else:
        print(False, '\n')


def not_gate():
    value_1 = int(input("Enter a value for A (1 or 0): "))
    print("Your inputs A =", value_1)
    if value_1 == 0:
        print(True, '\n')
    else:
        print(False, '\n')


main()
