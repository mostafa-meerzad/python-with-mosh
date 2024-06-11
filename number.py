import math


num = 10

x = 0b10  # 0b followed by a binary number, representation of literal binary numbers
print(x)
# bin(num) function return the binary representation of given number
print(bin(x))
print(bin(2))

y = 0x12c  # 0x followed by a hexadecimal number, representation of literal hexadecimal numbers
print(y)
# hex(num) function return the hexadecimal representation of given number
print(hex(y))
print(y)

# a + bi
z = 1 + 2j
print(z)
# ---------------------------------

a = 1 + 2
a = 1 - 2
a = 1 * 2
a = 1 / 2  # floating-point division
a = 1 // 2
a = 1 % 2  # remainder or modulus
a = 1 ** 2  # exponentiation

a += 1
a -= 1
a *= 1
a /= 1.5
a //= 1
a %= 1
a **= 1

# all above are the same pattern as following

a = a + 1
a = a * 1
a = a // 1

# ------------------------------

x = 3.49
print(math.floor(x))
print(math.ceil(x))
print(round(x))
print(abs(x))
print(math.pi)
