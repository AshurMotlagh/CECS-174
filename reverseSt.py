def reverseString(a_str):
    a_str_list = a_str.split(" ")
    new_a_string = ''
    every_other_word = 0
    for i in a_str_list:
        if every_other_word % 2 == 0:
            new_a_string = new_a_string + " " + i[::-1]
        else:
            new_a_string = new_a_string + " "+ i
        every_other_word += 1
    # print(new_a_string)
    new_a_string = new_a_string[1:]
    return new_a_string

if __name__ == '__main__': ## for your module test
    print(reverseString(input("Enter a sentence: ")))
