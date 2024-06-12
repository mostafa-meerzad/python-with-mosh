def fizzBuzz(num):
    if (num % 3 == 0) and (num % 15 == 0):
        return "Fizz Buzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return num


print(fizzBuzz(1))
print(fizzBuzz(3))
print(fizzBuzz(15))
print(fizzBuzz(5))
