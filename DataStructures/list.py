letters = ["a", "b", "c", "d",]  # list of strings
matrix = [[1, 4], [4, 5], [4, 4]]  # nested list
zeros = [0] * 5  # a list with 5 Zeros
combined = letters + zeros  # concatenate two lists

# `list` function takes an iterable object and turns it into a list
# list of numbers starting from 0 to 5, range logic applies here
generatedNumList = list(range(5))
generatedLetters = list("something new")

print(letters)
print(matrix)
print(zeros)
print(combined)
print(list(range(5)))
print(combined + list("1000"))
print(generatedNumList)
print(generatedLetters)

myList = [1, 2, 3, 5, 6]

firstElement = myList[0]

lastElement = myList[-1]

myList[0] = "String"
print(myList)


letters = ["a", "b", "c"]

letters[0] = "A"

# starting index is inclusive but the end index is exclusive thus the output is => ["A", 'b']
print(letters[0:-1])
print(letters[:])  # start and end omitted => all the list elements
print(letters[:3])  # start omitted default 0
print(letters[1:])  # end omitted default (list-length - 1)
# start form 0 end at third element (index 2) which is excluded
print(letters[0:2])
print(letters[::2])  # the third element is step

numbers = list(range(20))
print(numbers[::2])  # results all the even numbers of the list
print(numbers[::-1])  # results all the list elements in reverse order
print(numbers)  # results all the even numbers of the list

# ---------------------------------------------------------------
print()

# we got a list with a fixed number of elements and need to extract each one
nums = [1, 2, 3,]
# here is how
# first = nums[0]
# second = nums[1]
# third = nums[2]

# this line results exactly the same as above, but if we don't have the same number of elements and variables on the left side we would get an error
# first, second, third = nums


# first, second = nums # and here is the error `ValueError: too many values to unpack (expected 2)`

# to fix this error we can put the unwanted elements in a separate array

first, second, *rest = nums
print(first)
print(second)
print(rest)


nums = [1, 2, 3, 5, 6, 7, 8]

first, second, *rest, secondLast, last = nums
print(first)
print(second)
print(rest)  # rest variable will hold all the remaining elements
print(secondLast)
print(last)

# ----------------------------------------
print()

letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

# need to iterate over elements of a list and get their indices as well

for index, letter in enumerate(letters):
    print(index)
    print(letter)

print()
# print(enumerate(letters))
# --------------------------------------------------------

letters = ["a", "b", "c"]
print("original list")
print(letters)
print()

# Add
letters.append("D")  # add an element at the end of a list
letters.insert(-20, "DD")  # add an element at a specified index of the list,
# "greater that list length translates to the end" and "less than 0 translates to 0"

print("after adding elements")
print(letters)
print()

# Remove
letters.pop()  # pop removes the last element form list and returning it
# pop can also take an idex which will remove that element and returning it
letters.pop(1)
letters.remove("DD")  # Remove first occurrence of value.
del letters[0]  # remove specified element from the specified list
del letters[0: 2]  # remove a range of elements from the specified list
letters.clear()  # removes all the elements of the specified list

print("after removing elements")
print(letters)
print()
#  --------------------------------------------------

letters = ["a", "b", "c", "d", "e", "f",]

# index() list method returns the index of specified element if exists otherwise throws an error "ValueError: 'aa' is not in list"
letters.index("a")
# to avoid getting ValueError do this
if "aa" in letters:
    print(letters.index("aa"))

letters.count("a")  # Return number of occurrences of value.

print(letters.count("a"))

# ---------------------------------------

numbers = [1, 5, 3, 7, 4, 9]
print("numbers before sorting")
print(numbers)

# numbers.sort() # sorting in ascending order by default, can take a `reverse` boolean argument which sorts in reverse order
# print(numbers)

sortedList = sorted(numbers, reverse=True)
print(sortedList)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


def sortItem(item):
    return item[1]


items.sort(key=sortItem, reverse=False)
print(items)

# -------------------
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

items.sort(key=lambda item: item[1], reverse=True)
print(items)


# --------------------------------
print()
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

x = map(lambda item: item[1], items) # => <map object at 0x000001D85026EC40>
# now you can loop thought this map object or convert to another datatype

x = list(map(lambda item: item[1], items))
print(x)

# ---------------------------------
print()
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

x = filter(lambda item: item[1] >= 10, items) # this lambda function return the item[1] if the result of the expression is Boolean True 
print(x)

x = list(filter(lambda item: item[1] >= 10, items))

print(x)

# ---------------------------------
print()
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

x = [item[1] for item in items]
print(x)

x = [item for item in items if item[1] >= 10]

print(x)

# ----------------------------------

