word = input('Enter a word: ')
middleIdx = len(word) // 2
if (len(word) % 2) == 0:
    ans = word[middleIdx - 1] + word[middleIdx]
else:
    ans = word[middleIdx]

print('Middle:', ans)