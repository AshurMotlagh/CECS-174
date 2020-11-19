grades = {}

while True:
    user = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit?").upper()
    if user == 'A':
        name = input("Enter the name of the student: ")
        if name in grades:
            print("Sorry, that student is already present.")
            continue
        else:
            grade = input("Enter the student's grade:")
            grades[name] = grade
            continue

    if user == "R":
        remove = input("What student do you want to remove?")
        if remove not in grades:
            print("Sorry, that student doesn't exist and couldn't be removed.")
            continue
        else:
            grades.pop(remove)
            continue

    if user == 'M':
        modify = input("Enter the name of the student to modify:")
        if modify not in grades:
            print("Sorry, that student doesn't exist and couldn't be modified.")
            continue
        else:
            print("The old grade is", grades[modify])
            new_grade = input("Enter the new grade: ")
            grades[modify] = new_grade
            continue

    if user == 'P':
        if len(grades) == 0:
            print("No record found!")
            continue
        else:
            for key in sorted(grades.keys()):
                print(key, grades[key])

    if user == 'Q':
        print("Goodbye!")
        break
