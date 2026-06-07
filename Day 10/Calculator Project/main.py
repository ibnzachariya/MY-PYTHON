import art
def add(n1, n2):
     return n1 + n2

my_fav_operation = add
print(my_fav_operation(4, 5))  #this will add 4 and 5

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

diction = {
    "+": add, "-": subtract, "*": multiply, "/": divide
}

# To use the dictionary operations to perform the calculations. Multiply 4 * 8 using
#print(diction["*"](4, 8))
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("what is the first number?"))

    while should_accumulate:
        for symbol in diction:
            print(symbol)
        operation_symbol = input("what is the operation?")
        num2 = float(input("what is the next number?"))
        answer = diction[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation" )

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
