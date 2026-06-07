def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6,7,8,9))

def calculate(n, **kwargs):
    print(kwargs)
    # for k, v in kwargs.items():
    #     print(k)
    #     print(v)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

    calculate(2, add=3, multiply=4)