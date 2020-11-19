import random
rand_num = (random.randint(1,11))
print("I am thinking of a number between 1 and 10.")
chance = 5

while True:
    user = int(input("Take a guess :"))
    if chance == 0:
        print("You guessed wrong, the number I was thinking of was", rand_num)
        break
    while chance > 0:
        if 1 < user > 10:
            user = int(input("Wrong value, re-enter:"))
            continue

        if user > rand_num:
            print("Your guess is too high.")
            chance -= 1
            user = int(input("Take a guess :"))
            continue

        elif user < rand_num:
            print("Your guess is too low.")
            chance -= 1
            user = int(input("Take a guess :"))
            continue

        elif user == rand_num:
            chance -= 1
            print("Good job, you got it with", 5 - chance, "guesses")
        break
    else:
        print("You guessed wrong, the number I was thinking of was", rand_num)
    break
