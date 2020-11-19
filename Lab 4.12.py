word = input("Enter a string:").lower()
inverse_word = word[::-1]
if word == inverse_word:
        print("Palindrome")
else:
        print("different word")
