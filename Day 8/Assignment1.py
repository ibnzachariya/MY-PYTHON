import random

# Room functions
def sitting_room():
    while True:
        print("\n--- Sitting Room ---")
        print("1. Watch TV")
        print("2. Read a book")
        print("3. Return to main menu")
        choice = input("Choose: ")
        if choice == "1":
            print("You are watching TV... 📺")
        elif choice == "2":
            print("You are reading a book... 📖")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def bedroom():
    while True:
        print("\n--- Bedroom ---")
        print("1. Sleep")
        print("2. Play video games")
        print("3. Return to main menu")
        choice = input("Choose: ")
        if choice == "1":
            print("You are sleeping... 😴")
        elif choice == "2":
            print("You are playing video games... 🎮")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def kitchen():
    while True:
        print("\n--- Kitchen ---")
        print("1. Cook food")
        print("2. Eat snacks")
        print("3. Return to main menu")
        choice = input("Choose: ")
        if choice == "1":
            print("You are cooking delicious food... 🍲")
        elif choice == "2":
            print("You are eating snacks... 🍪")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def restroom():
    while True:
        print("\n--- Rest Room ---")
        print("1. Take a shower")
        print("2. Brush teeth")
        print("3. Return to main menu")
        choice = input("Choose: ")
        if choice == "1":
            print("You are taking a shower... 🚿")
        elif choice == "2":
            print("You are brushing your teeth... 🪥")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def car_park():
    while True:
        print("\n--- Car Park ---")
        print("1. Wash car")
        print("2. Drive car")
        print("3. Return to main menu")
        choice = input("Choose: ")
        if choice == "1":
            print("You are washing your car... 🚗🧽")
        elif choice == "2":
            print("You are driving your car... 🚙💨")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

# MAIN PROGRAM
print("Welcome! Please guess a number between 1 and 5 to enter my house.")

secret_number = random.randint(1, 5)
guess = int(input("Your guess: "))

if guess == secret_number:
    print("Correct! 🎉 Welcome to my house 🏠")

    while True:
        print("\n--- Main Menu ---")
        print("1. Sitting Room")
        print("2. Bedroom")
        print("3. Kitchen")
        print("4. Rest Room")
        print("5. Car Park")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            sitting_room()
        elif choice == "2":
            bedroom()
        elif choice == "3":
            kitchen()
        elif choice == "4":
            restroom()
        elif choice == "5":
            car_park()
        elif choice == "6":
            print("Goodbye! Thanks for visiting my house. 👋")
            break
        else:
            print("Invalid choice!")

else:
    print("You Do Not Have Access To My House 🚫")
