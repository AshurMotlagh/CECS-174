num1 = [1,2,3,4,5,6,7,8,9,0]
num_str = str(num1)
num_str = num_str[1:-1]

print(num_str)



print("Every other element of the random list (keep the first element):")


print("The value of elements that are even:")
even_list = []
for i in num1:
    if (i // 2) == 0:
        even_list.append(i)
even = str(even_list)
even = even[1:-1]
even.rstrip(',')
print(even_list)