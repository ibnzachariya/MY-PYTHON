import random
# option1
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

#option2
random_index = random.randint(0, 4)
print(friends[random_index])