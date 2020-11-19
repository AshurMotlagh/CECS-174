def testForAnagram(x, y):
    total = 0
    if len(x) != len(y):
        return "Different words"
    else:
        for i in range(len(x)):
            for o in range(len(y)):
                if x[i] == y[o]:
                    total += 1
                    break
        if total == len(x):
            return "Anagram"
        else:
            return "Different words"