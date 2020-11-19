grades = {}
good  = ['A', 'B', 'C', 'D', 'F']
while True:
    user = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit?").upper()

    if user == 'A':
        name = input("Enter the name of the student: ")
        if name in grades:
            print("Sorry, that student is already present.")

        else:
            try:
                grade = input("Enter the student's grade:").upper()
                if grade[0] not in good:
                    raise ValueError("Invalid grade, did not add record. Valid grades are 'A','B','C','D','F' !")
            except ValueError as e:
                print(e)
            else:
                grades[name] = grade

    if user == "R":
        remove = input("What student do you want to remove?")
        try:
            grades.pop(remove)
        except:
            print("Sorry, that student doesn't exist and couldn't be removed.")

    if user == 'M':
        modify = input("Enter the name of the student to modify:")
        if modify not in grades:
            print("Sorry, that student doesn't exist and couldn't be modified.")

        else:
            print("The old grade is", grades[modify])
            new_grade = input("Enter the new grade: ")
            grades[modify] = new_grade

    if user == 'P':
        for key in sorted(grades.keys()):
                print(key, grades[key])

    if user == 'Q':
        print("Goodbye!")
        break
