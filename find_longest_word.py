def findLongestWord(a_str):
    a_str_split = a_str.split()
    x = 0
    max = a_str_split[0]
    for i in range(0,len(a_str_split)):
        if len(max) <= len(a_str_split[i]):
            max = a_str_split[i]
    return max

if __name__ == '__main__': ## for your own module test
    print(findLongestWord(input("Enter a sentence: ")))