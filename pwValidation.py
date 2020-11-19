# def main():
#     count = 3
#     user = input("Enter a new password:")
#     while count > 0:
#         if validatePassword(user) is False:
#             print("Your password does not meet complexity requirements!")
#             count -= 1
#             user = input("Enter a new password:")
#             continue
#         retry = input("Please re-enter the same password:")
#         if retry == user:
#             print("Password is valid and two entries are matching")
#             break
#         if retry != user:
#             print("Passwords do not match!")
#             count -= 1
#             user = input("Enter a new password:")
#             continue
#
#         if count == 0:
#             print("You have not provided a valid password, goodbye!")
#             break
def main():
    attempts = 0
    while True:
        if attempts < 3:
            user = input("Enter a new password: ")
            if validatePassword(user) is False:
                print("your password does not meet complexity requirements")
                attempts += 1
                continue
            else:
                validation = input("Please re-enter the same password: ")
                if validation == user:
                    print("Password is valid and two entries are matching")
                    break
                else:
                    print("Passwords do not match!")
                    attempts += 1
                    continue
        else:
            print("You have not provided a valid password, goodbye!")
            break


def validatePassword(password):
    if len(password) < 8:
        return False
    haslower = False
    hasupper = False
    for ch in password:
        if ch.islower():
            haslower = True
        if ch.isupper():
            hasupper = True
    if password.isalnum() and haslower and hasupper:
        return True
    else:
        return False


main()

#
# def validatePassword(password):
#     if len(password) < 8:
#         return False
#
#     hasLower = False
#     hasUpper = False
#     hasDigit = False
#     for ch in password:
#         if ch.islower():
#             hasLower = True
#         if ch.isupper():
#             hasUpper = True
#         if ch.isdigit():
#             hasDigit = True
#
#     return password.isalnum() and hasLower and hasUpper and hasDigit
#
#
# def main():
#     attempts = 0
#     retry = False
#     oldPassword = None
#
#     while attempts < 3:
#         if retry:
#             password = input("Please re-enter the same password:")
#
#             if password == oldPassword:
#                 print("Password is valid and two entries are matching")
#                 return
#             else:
#                 print("Passwords do not match!")
#                 retry = False
#         else:
#             password = input("Enter a new password:")
#
#             if not validatePassword(password):
#                 print("Your password does not meet complexity requirements!")
#             else:
#                 oldPassword = password
#                 retry = True
#         attempts += 1
#     print("You have not provided a valid password, goodbye!")
#
#
# main()