file_name = input("Enter the input file name: ")
my_file = open(file_name)
line = my_file.readlines()
lines = len(line)
words = 0
characters = 0
for i in line:
    word_list = i.split()
    words += len(word_list)
    for j in i:
        if j != ' ':
            characters += 1
print("The file contains", characters, 'characters,', words, 'words and', lines, 'lines')