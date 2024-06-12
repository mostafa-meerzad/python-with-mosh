def increment(number, by):
    print("incrementing...")
    return number + by
    return (number, by, number + by)


print(increment(100, 1))


def myFunction():
    pass


print(myFunction())


def increment(number, by):
    print("incrementing...")
    return number + by
    return (number, by, number + by)


print(increment(100, by=2))


def increment(number, by=10):
    print("incrementing...")
    return number + by
    return (number, by, number + by)


print(increment(100))  # by argument is not specified
print(increment(100, 2))


def increment(number: int, by: int = 10) -> int:
    print("incrementing...")
    return number + by
    return (number, by, number + by)


print(increment(100))  # by argument is not specified
print(increment(100, 2))


def increment(number: int, by: int = 10) -> list:
    print("incrementing...")
    return (number, number + by)


print(increment(100))  # by argument is not specified
print(increment(100, 2))

def argFunction(*args):
    for x in args:
        print(x)

argFunction(1,1,2,3,5,6,7,7)

def saveUser(**kwargs):
    print(kwargs)
    print(kwargs["id"]) # access the id of the provided user


saveUser(id=10, name="John", last="Smith")