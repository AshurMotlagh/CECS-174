input_1 = input("Enter the first set of integer values separated by space:")
input_2 = input("Enter the second set of integer values separated by space:")
list1 = input_1.split()
list2 = input_2.split()
list1.sort()
list2.sort()

print("Checking if the two lists are the same :")

if input_2 == input_1:
    print("Yes, they are.")
else:
    print("They are not.")

print("Checking if the two lists contain the same elements:")

if list1 == list2:
    print("Yes, they are.")
else:
    print("They are not.")