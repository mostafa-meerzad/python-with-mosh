# first = 100
# second = 0

# try:
#     print(first / second)

# except ZeroDivisionError:
#     print("cannot divide by zero!")

# else:
#     print("congrats no exception occurred")

# finally:
#     print("let's say something any way")


# def my_exception():
#     raise ValueError("my value error")


# # my_exception()


# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age Cannot be 0!")

#     return age / 10


# calculate_xfactor(0)

#
# try:
#     file = open("./raiseCost.py")
#     age = int(input("age: "))
#     xfactor = 10 / age
#     print(file)
#
# except (ValueError, ZeroDivisionError):
#     print("you didn't enter a valid age")
#
# else:
#     print("no exception was thrown")
#
# finally:
#     file.close()
# ------------------------- opening file using "with" statement ----------------------
try:
    with open("./raiseCost.py") as file:
        print("file opened.")
    age = int(input("age: "))
    xfactor = 10 / age

except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")

else:
    print("no exception was thrown")
