# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")
print("Asalamualeikum")
height = int(input("Enter your height in centimeters: "))

if height >= 120:
    print("You can proceed")
    age = int(input("Age please? "))
    if age >= 10:
      print("Pay $2.")
    elif age <= 16:
      print("pay $4.")
    elif age <= 20:
      print("pay $6.")
    else:
      print("pay $8.")
else:
 print("Sorry no access")