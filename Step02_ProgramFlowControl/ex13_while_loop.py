import random

highest = 10
answer = random.randint(1, highest)

print("Please input number between 1 and {}: ".format(highest))
guess = int(input())


def check_correct(guess):
    if guess == answer:
        print("You guess it correct")
    elif guess == 0:
        print("Too bad you are a quitter")
        exit()


while guess != answer:
    if guess < answer:
        print("Please guess higher")
        guess = int(input())
        check_correct(guess)
    else:
        print("Please guess lower")
        guess = int(input())
        check_correct(guess)
