import random

def check_guess(guess, secret_number):
    if guess > secret_number:
        print("Sorry, Too high")
        return False
    elif guess < secret_number:
        print("Sorry, Too low")
        return False
    else:
        print("Correct! You win! Well done!")
        return True

secret_number = random.randint(1, 20)
lives = 5

while lives > 0:
    guess = int(input("Guess a number between 1 and 20: "))
    if check_guess(guess, secret_number):
        break
    else:
        lives -= 1
        print(f"Lives left: {lives}")

if lives == 0:
    print("Game over! You ran out of lives.")
