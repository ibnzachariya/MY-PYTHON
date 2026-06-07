import random

def crop_field():
    while True:
        print("\n--- Crop Field ---")
        print("1. See maize")
        print("2. See rice")
        print("3. See yam")
        print("4. Return to farm menu")
        choice = input("Choose: ")
        if choice == "1":
            print("You see tall green maize plants ready for harvest! 🌽")
        elif choice == "2":
            print("You see golden rice fields swaying in the wind! 🌾")
        elif choice == "3":
            print("You see yam mounds with fresh leaves! 🍠")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def animal_pen():
    while True:
        print("\n--- Animal Pen ---")
        print("1. See chickens")
        print("2. See goats")
        print("3. See cows")
        print("4. Return to farm menu")
        choice = input("Choose: ")
        if choice == "1":
            print("Cluck cluck! The chickens are pecking at the ground. \n🐓🐓🐓🐓🐓")
        elif choice == "2":
            print("The goats are bleating happily. \n🐐🐐🐐🐐")
        elif choice == "3":
            print("The cows are grazing peacefully. \n🐄🐄🐄🐄🐄")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def sales_shop():
    while True:
        print("\n--- Farm Sales Shop ---")
        print("1. Buy maize")
        print("2. Buy rice")
        print("3. Buy yam")
        print("4. Buy eggs")
        print("5. Return to farm menu")
        choice = input("Choose: ")
        if choice == "1":
            print("You bought a bag of maize! 🌽")
        elif choice == "2":
            print("You bought a sack of rice! 🌾")
        elif choice == "3":
            print("You bought some fresh yams! 🍠")
        elif choice == "4":
            print("You bought a crate of eggs! 🥚")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

# MAIN PROGRAM
print("Welcome to Abdulfatai's Farm! 🌾🐓🍠")

# Guessing game before entry
secret_number = random.randint(1, 5)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 5 to enter the farm: "))
    if guess != secret_number:
        print("Wrong guess! Try again.")

print("Correct! 🎉 You may explore the farm.")

while True:
    print("\n--- Farm Menu ---")
    print("1. Explore Crop Field")
    print("2. Visit Animal Pen")
    print("3. Go to Sales Shop")
    print("4. Exit Farm")

    choice = input("Choose: ")

    if choice == "1":
        crop_field()
    elif choice == "2":
        animal_pen()
    elif choice == "3":
        sales_shop()
    elif choice == "4":
        print("Goodbye! Thanks for visiting the farm. 👋")
        break
    else:
        print("Invalid choice!")
