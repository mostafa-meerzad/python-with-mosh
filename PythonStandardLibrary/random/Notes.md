# Random Values

```py
import random
import string

print(random.random())  # generate a random value in (0, 9)
print(random.randint(0, 10))  # generate a random value in (0, 10)
print(
    random.choice([1, 2, 5, 7, 8])
)  # an iterable is given and a random value is picked
print(
    random.choices([1, 2, 5, 7, 8], k=2)
)  # an iterable is given and "k" number of random value is picked

myPassword = "".join(
    random.choices("abcdefghi", k=4)
)  # use string.join(iterable) method to get a string instead of individual characters
print(myPassword)
# the above method to generate password is good but we lack the number of choices for the character to form the password
myStrongPassword = "".join(random.choices(string.ascii_letters + string.digits, k=4))

print(myStrongPassword)

# the string module has some useful methods
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(
    string.capwords("mostafa meerzad")
)  # to capitalize the given string, Mostafa Meerzad
print(string.hexdigits)  # 0123456789abcdefABCDEF
print(string.octdigits)  # 01234567
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

```
