file_name = input("Enter the input file name: ")
file1 = open(file_name)
file1_read = file1.readlines()
file1.close()
file2 = open("100-most-common-words.txt", 'r')
file2_read = file2.readlines()
file2.close()
list = []
# # read all file first
# # use for loop to read the each word , save --> look up table
print("The following words are not in the 100 most common word list:")

for wd in file2_read:
    wd = wd.rstrip()
    list.append(wd)

for wd2 in file1_read:
    wd2_list = wd2.split()
    for k in wd2_list:
        if k not in list:
            print(k)
# file1_read = file1.readlines()
# # read single line # your file
# # find the word in file # check if this word is in the look up table
# # then print that word