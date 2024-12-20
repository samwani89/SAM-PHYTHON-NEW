import random

def guess_the_number():
    number_to_guess = random.randint(1, 50)
    while True:
        guess = int(input("Guess a number between 1 and 50: "))
        if guess == number_to_guess:
            print("Your guess is right! 🎉")
            break
        else:
            print("Your guess is wrong. Try again!")

guess_the_number()
