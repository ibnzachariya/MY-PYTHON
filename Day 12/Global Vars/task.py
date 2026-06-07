# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies #the word global is used when you wanna tap in and use a global scope in a function
    # the return function can be used
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


