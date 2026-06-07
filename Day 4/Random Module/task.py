import random
# import My_module
# where My_module folder has been created under the random module

# my_age = random.randint(1, 10)
# print(my_age)
#Gives a randon number each time it is run

# print(My_module.my_favorite_number)
# my_favorite_number is the variable name in the my_module folder

# https://docs.python.org/3/library/random.html
random_heads_or_tails = random.randint(1, 5)
if random_heads_or_tails == 1:
    print("Tails")
else:
    print("Heads")
