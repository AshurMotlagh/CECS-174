# Read input from the user.
word = input("Enter a word: \n")

if word.isalpha():
    print('The word contains only letters.')

if word.isupper():
    print("All string in the word are uppercase letters.")

if word.islower():
    print("All string in the word are lowercase letters.")

if word.isdigit():
    print('The word contains only digits.')

if word.isalnum():
    print('The word contains either letters or numbers.')

if word[0].isupper():
    print("The word starts with a capital letter.")

if word.endswith("."):
    print('The word ends with a period.')