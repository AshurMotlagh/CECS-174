grade = input("Enter a letter grade: ").upper()

if grade[0] == "A":
    num = 4.0

elif grade[0] == "B":
    num = 3.0

elif grade[0] == "C":
    num = 2.0

elif grade[0] == "D":
    num = 1.0

else:
    num = 0.0

if len(grade) > 1 and grade[0] != "F":
    if grade[1] == "+" and grade[0] != "A":
        num = num + .3
    elif grade[1] == "-":
        num = num - .3
print("The numeric value is", num)
