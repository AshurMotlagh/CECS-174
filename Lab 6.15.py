user_input = int(input("Enter a number to draw triangle: \n"))
i = 1
total = user_input - 1

while i <= user_input:
    print('*' * i)
    i = i+1
    if i == 0:
        break

while total <= (user_input * 2):
    print('*' * total)
    total = total - 1
    if total == 0:
        break
