import random

def guess_number():
    number = random.randint(1, 20)
    while True:
        guess = int(input("Please Guess a number between 1 and 20: "))
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("Correct! You guessed it.")


guess_number()
