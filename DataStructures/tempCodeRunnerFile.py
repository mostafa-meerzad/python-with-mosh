x = 1
y = 2
print("before swap")
print("x ", x)
print("y ", y)
# to swap two variables we need a third variable
z = x
x = y
y = z
print("after swap")
print("x ", x)
print("y ", y)

# python way

x = 1
y = 2
print("before swap")
print("x ", x)
print("y ", y)
x, y = y, x
print("after swap")
print("x ", x)
print("y ", y)
