sentence = input("Enter a sentence: \n")
x=sentence
lower_vowel = "aiou"
upper_vowel = "AIOU"
for each in sentence:
    if each in lower_vowel:
        x = x.replace(each, "e")
    if each in upper_vowel:
        x = x.replace(each, "E")
print(x)