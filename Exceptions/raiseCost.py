from timeit import timeit

first = """

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age Cannot be 0!")
    
    return age / 10

try:
    calculate_xfactor(0)
except ValueError:
    pass
    # print("age cannot be zero")

"""
second = """

def calculate_xfactor(age):
    if age <= 0:
        # raise ValueError("Age Cannot be 0!")
        return None
    return age / 10

result = calculate_xfactor(0)
if result == None:
    pass
    # print("got no results")

"""

print(timeit(first, number=1000))
print(timeit(second, number=1000))
