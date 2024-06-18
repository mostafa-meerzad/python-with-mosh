myDict = {"name":"Mostafa", "age":24, "job":"SE"}

my_dict = dict(name="mostafa", age=24)

print(myDict)
print(my_dict)
del myDict["name"]
print(myDict)
print(my_dict)
myDict["salary"] = "2000"
print(myDict)
# print(my_dict["a"])

for x in myDict:
    print(x)
    print(myDict[x])

for k, v in myDict.items():
    print(k, v)