from pathlib import Path


myList = [1,2,3,5, "something"]

print(myList.count(1))
print(myList.append(55))
print(myList)
myList.insert(2, 550)
print(myList)
print(myList.remove(2))
print(myList)
# myList.clear()
print(myList)

newList = myList + [2,3,5,5,5,55,]
print(newList)

print("---------------------")

# print(myList[100])

print("=================================================")

path = Path()
for p in path.iterdir():
    print(p)