from sys import getsizeof

values = (x for x in range(100))

print(values)

# for x in values:
# print(x)


print(getsizeof(values))
print(getsizeof([x for x in range(100)]))
