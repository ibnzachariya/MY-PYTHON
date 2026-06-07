print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("youth ticket is $7.")
    else:
        bill = 12
        print("adult ticket is $12.")

    plus_photo = input("Would you like to want a photo? (y/n)")
    if plus_photo == "y":
        bill += 3

        print(f"Your total bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
