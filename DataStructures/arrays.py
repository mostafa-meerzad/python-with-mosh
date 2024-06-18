from array import array

arr = array("i", [1,2,4,5,6,7])

print(arr)

for x in arr:
    print(x)

arr[0] = 11

print(arr)
arr.append(22)
print(arr)
arr.extend([55, 66, 88])
print(arr)
arr.insert(3, 33)
print(arr)
arr.remove(33)
print(arr)
arr.pop()
print(arr.pop())
print(arr)
