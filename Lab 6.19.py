text = input("Enter a string: ")

print("Only uppercase letters in the string : ", end='')
for letter in text:
    if letter.isupper():
        print(letter, end='')

print("\nEvery second letter/number in the string: ", end='')
for i in range(1, len(text), 2):
    print(text[i], end="")

print("\nReplacing all the vowels with underscore: ", end="")
for vowel_replace in range(0,len(text)):
    if text[vowel_replace].lower() == 'a' or text[vowel_replace].lower() == 'e' or text[vowel_replace].lower() == 'i' or text[vowel_replace].lower() == 'o' or text[vowel_replace].lower() == 'u':
        print('_', end='')
    else:
        print(text[vowel_replace], end='')

digit = 0
for num in range(len(text)):
    if text[num].isdigit():
        digit += 1
print("\nThe total number of digits in the string:", digit)

print("The positions of all the vowels in the string: ",end="")
for vowel_num in range(0,len(text)):
    if text[vowel_num].lower() == 'a' or text[vowel_num].lower() == 'e' or text[vowel_num].lower() == 'i' or text[vowel_num].lower() == 'o' or text[vowel_num].lower() == 'u':
        print(vowel_num, end=' ')