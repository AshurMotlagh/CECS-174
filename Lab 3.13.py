##
#  Print the first 3 letters of a string, followed by ..., followed by the  last 3 letters of a string.
##

word = input("Enter a word with longer than 8 letters: ")

print("The new word is", word[0:3], "...", word[-3:])