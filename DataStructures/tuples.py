tuple1 = 1, 2, 3, 4
tuple2 = (1, 2, 3, 4)
tuple2 = ("1st", "2nd", "3th", "4th")

print(tuple1)
print(tuple2)
print(tuple1[1])

singletonTuple = 1  # value 1
singletonTuple = (1,)  # tuple containing 1
singletonTuple = (1,)  # tuple containing 1

print(singletonTuple)

tuple3 = tuple1 * 4
tuple4 = tuple1 + tuple2
tuple5 = tuple1 + tuple2 * 2

print(tuple3)
print(tuple4)
print(tuple5)

first, second, third, *rest = tuple2

print(first)
