# project1_rps_Motlagh.py
#
# Name(s): Ashur Motlagh
#
# Date: 9 / 21 / 19
#
#
answer_list = ['rock', 'paper', 'scissors']


def main():
    loop_exit = True
    print("In this program you will be playing \"Rock Paper and Scissors\" with a 33.33% chance of winning")
    while loop_exit:
        user_answer = input("Rock! Paper! Scissors!: ").lower()  # here we are asking user for their response

        while user_answer not in answer_list:  # this is input verification
            print("User input is wrong")
            break

        # while answer == 'rock' or answer == "paper" or answer == 'scissors':
        while user_answer in answer_list:
            comp = rps()  # here we are calling the function rps, computers choice
            print("System chose:", comp, "You chose:", user_answer)  # displaying what user and computer chose

            # here is the process of who wins / loses / tie
            if comp == 'paper':
                if user_answer == comp:
                    print("Tie")
                elif user_answer == 'rock':
                    print("You lose. Paper beats Rock.")
                elif user_answer == 'scissors':
                    print("You win. Scissors beats Paper")

            elif comp == 'rock':
                if user_answer == comp:
                    print("Tie")
                elif user_answer == 'paper':
                    print("You win. Paper beats Rock")
                elif user_answer == 'scissors':
                    print("You lose. Rock beats Scissors")

            elif comp == 'scissors':
                if user_answer == comp:
                    print("Tie")
                elif user_answer == 'paper':
                    print("You lose. Scissors beats Paper")
                elif user_answer == 'rock':
                    print("You win. Rock beats Scissors")

            flag = input("\nDo you want to continue? (Y/N) ").upper()  # flag is going to be the "continue" option
            if flag[0] == 'Y':
                user_answer = input("Rock! Paper! Scissors!: ").lower()  # asking what for their choice again
            else:
                loop_exit = False
                break
        if not loop_exit:
            break


def rps():  # here we are doing the probability of winning and computer's choice
    num = number()  # here we are getting the results of the number function and applying it to the computers choice
    if num <= 25:
        comp = 'paper'

    elif 26 <= num <= 50:
        comp = 'rock'


    else:
        comp = 'scissors'
    return comp  # returning the computer's choice to the main function


def number():  # this is the function for getting the random number for the function rps
    import random
    for x in range(1):
        rand_num = (random.randint(1, 76))
        return rand_num  # returning the random numbers to the rps function


main()
