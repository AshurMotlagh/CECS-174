grade = (input("Enter a grade or -1 to finish: \n"))
pass_counter = 0
fail_counter = 0
grade_list = []
grade_list.append(int(grade))
if int(grade) >= 70:
    pass_counter += 1

elif int(grade) < 70 and int(grade) >= 0:
    fail_counter += 1

while grade >= '0':
    grade = input("Enter a grade or -1 to finish: \n")
    if int(grade) >= 70:
        pass_counter += 1

    elif int(grade) < 70 and int(grade) >= 0:
        fail_counter += 1

    if grade >= '0':
        grade_list.append(int(grade))

average = sum(grade_list)/len(grade_list)
print("The average grade is ", format(average, '.2f'))
print("Number of passing grades is", pass_counter)
print("Number of failing grades is", fail_counter)
print("The maximum grade is ", max(grade_list))
print("The minimum grade is ", min(grade_list))



