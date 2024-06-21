first = 100
second = 0

try:
    print(first / second)

except ZeroDivisionError:
    print("cannot divide by zero!")

else:
    print("congrats no exception occurred")

finally:
    print("let's say something any way")


def my_exception():
    raise ValueError("my value error")


# my_exception()


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age Cannot be 0!")
    
    return age / 10


calculate_xfactor(0)