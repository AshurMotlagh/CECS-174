def list_from_file(file_name):
    try:
        my_file = open(file_name)
        line_list = my_file.readlines()
        my_list = []
        for i in line_list:
            my_list.append(i.rstrip())
        return my_list

    except FileNotFoundError as e:
        return(e)



def main():
    file_name = input("Enter the input file name: ")
    print(list_from_file(file_name))


main()