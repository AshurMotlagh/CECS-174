#  Define constants.

##### Use the given variable "NAMES" as is, and DO NOT CHANGE its type, format and contents #######

NAMES = "January,  February March   April,  May      June     July     August   September October  November December        "

no_comma = NAMES.replace(','," ")
month = int(input('Enter a number between 1 and 12: '))
list_names = no_comma.split()

if month <= 0 or month > 12:
    print("ERROR")
else:
    print(month, "is", list_names[month - 1])
