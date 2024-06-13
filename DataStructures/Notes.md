# Data Structures

## List

A **list** is a data-type showing a list of objects, element types doesn't matter it can be of any type

```py

letters = ["a", "b", "c", "d",]
matrix = [[1, 4], [4, 5], [4, 4]]
zeros = [0] * 100

print(letters)
print(matrix)
print(zeros)
```

if you need a list of repeated value do this `[element] * number` `zeros = [0] * 10` this will create a list containing 10 zeros

```py
letters = ["a", "b", "c", "d",] # list of strings
matrix = [[1, 4], [4, 5], [4, 4]] # nested list
zeros = [0] * 5 # a list with 5 Zeros
combined = letters + zeros # concatenate two lists

# `list` function takes an iterable object and turns it into a list
generatedNumList = list(range(5)) # list of numbers starting from 0 to 5, range logic applies here
generatedLetters = list("something new")

print(letters)
print(matrix)
print(zeros)
print(combined)
print(list(range(5)))
print(combined + list("1000"))
print(generatedNumList)
print(generatedLetters)
```

### Accessing Items

lists are 0 based index and its elements is accessed using `listName[index]`, index 0 is the first element` list-length - 1` is the last element, positive index gives element form start to end, negative index give element form the end

```py
myList = [1,2,3,5,6]

firstElement = myList[0]

lastElement = myList[-1]

myList[0] = "String"
print(myList)
```

you can slice a list as well

```py
letters = ["a", "b", "c"]

letters[0] ="A"

print(letters[0:-1])
```

you can specify a `step` as well

```py
numbers = list(range(20))
print(numbers[::2])  # results all the even numbers of the list
print(numbers[::-1])  # results all the list elements in reverse order
print(numbers)  # results all the even numbers of the list

```

### Unpacking Lists

imagine a situation that we got a list with a fixed number of elements and need to extract each one

`accessing and assigning each element individually`

```py
nums = [1, 2, 3,]
# here is how
first = nums[0]
second = nums[1]
third = nums[2]
```

`unpacking list elements`

```py
nums = [1, 2, 3,]

first, second, third = nums # this line results exactly the same as above, but if we don't have the same number of elements and variables on the left side we would get an error
```

but the above approach has a problem, if the number of variables on the left-side is not the same as the number of elements in the list we will get a `ValueError`

```py
nums = [1, 2, 3,]

first, second = nums # and here is the error `ValueError: too many values to unpack (expected 2)`
```

`to fix this error we can put the unwanted elements in a separate array`

```py
nums = [1, 2, 3,]

first, second, *rest = nums
print(first)
print(second)
print(rest) # rest variable will hold all the remaining elements

```

`if you need some elements from the beginning and some from the end of a list`

```py
nums = [1, 2, 3, 5, 6, 7, 8]

first, second, *rest, secondLast, last = nums
print(first)
print(second)
print(rest) # rest variable will hold all the remaining elements
print(secondLast)
print(last)
```

### Looping over lists

```py
letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

```

need to iterate over elements of a list and get their indices as well, use `enumerate()` function which returns an iterable object of tuples for each list element and it's index like so `(index, element)`

```py
letters = ["a", "b", "c"]

for x in enumerate(letters):
    print(x) # would be (index, element)
    print(x[0]) # would be index
    print(x[1]) # would be element

# but here is a better way, using list-unpacking which amazingly works for `tuples`

for index, element in enumerate(letters):
    print(index) # would be index
    print(element) # would be element

```

### Adding/Removing items

```py

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

```

```py

# Remove
letters.pop() # pop removes the last element form list and returning it
letters.pop(1) # pop can also take an idex which will remove that element and returning it
letters.remove("DD") # Remove first occurrence of value.
del letters[0] # remove specified element from the specified list
del letters[0: 2] # remove a range of elements from the specified list
letters.clear() # removes all the elements of the specified list

print("after removing elements")
print(letters)
print()

```

### Finding items

```py
letters = ["a", "b", "c", "d", "e", "f",]

# index() list method returns the index of specified element if exists otherwise throws an error "ValueError: 'aa' is not in list"
letters.index("a")
# to avoid getting ValueError do this
if "aa" in letters:
    print(letters.index("aa"))

letters.count("a")  # Return number of occurrences of value.

print(letters.count("a"))

```

### Sorting lists

**basics**

for basic sorting the `sort()` list method is sufficient it modifies the original list and can define the sorting order `reverse=True` sorts the list in reverse order otherwise sorts in ascending order by default

```py

numbers = [1, 5, 3, 7, 4, 9]
print("numbers before sorting")
print(numbers)

numbers.sort() # sorting in ascending order by default, can take a `reverse` boolean argument which sorts in reverse order
print(numbers)

# sorted function takes an iterable and sorts it in ascending order
sortedList = sorted(numbers, reverse=True)
print(sortedList)

```

**advanced**

sorting complex objects is different:

1. define a function that parses the part of object you want to sort based on that
2. give that function to `sort()` list method as a keyword-argument

```py
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

def sortItem(item):
    return item[1]

items.sort(key=sortItem, reverse=True)
print(items) # [('product3', 12), ('product1', 10), ('product2', 9)]

items.sort(key=sortItem)
print(items) # [('product2', 9), ('product1', 10), ('product3', 12)]

```

### Lambdas

a lambda function is an **anonymous** function which is basically a function declared in a single line

**syntax**

`lambda parameters:expression` lambda functions return the result of expression by default, no need to explicitly return a value

```py
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

items.sort(key=lambda item:item[1])
print(items)
```

### Map Function

`map(fn, iterable)` function performs an operation on each element of an iterable and returns an map-object which is an iterable and we can iterate over or convert to another dataType.

```py
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

x = map(lambda item: item[1], items) # => <map object at 0x000001D85026EC40>
# now you can loop thought this map object or convert to another datatype

x = list(map(lambda item: item[1], items)) # a list of each item's second element
print(x)

```

### Filter Function

`filter(fn, iterable)` function takes a function which is executed on each element of that iterable and returns a **filter object** which is an iterable and then can be converted to a **list** and that way we would have a filtered list

```py
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

x = filter(lambda item: item[1] >= 10, items) # this lambda function return the item[1] if the result of the expression is Boolean True
print(x) # <filter object at 0x0000013B3D6FECD0>

x = list(filter(lambda item: item[1] >= 10, items))
print(x) # [('product1', 10), ('product3', 12)]
```

### List Comprehension

Python list comprehension is a concise way to create lists. It allows for the generation of a new list by applying an expression to each item in an existing iterable (like a list or a range) and optionally filtering items that meet a condition. The syntax is simpler and more readable than traditional loops and list operations.

```py
[new_item for item in iterable if condition]
```

- `new_item`: The expression for the new items in the resulting list.
- `item`: The variable representing each element in the iterable.
- `iterable`: The collection (e.g., list, range) to iterate over.
- `condition (optional)`: A filtering condition that determines whether an item is included in the new list.

```py
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

x = [item[1] for item in items]

print(x)
```

### Zip Function

The `zip()` function in Python is used to combine elements from multiple iterables (like lists, tuples, or sets) into tuples. Each tuple contains one element from each of the iterables. Here's a detailed explanation:

#### Syntax

```python
zip(*iterables)
```

#### Parameters

- `*iterables`: This indicates that `zip` can take one or more iterable arguments.

#### Behavior

- The `zip()` function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.
- The iterator stops when the shortest input iterable is exhausted. This means that if the provided iterables are of different lengths, `zip()` stops creating tuples when the shortest iterable is exhausted.

#### Examples

1. **Basic Example with Two Lists**

   ```python
   list1 = [1, 2, 3]
   list2 = ['a', 'b', 'c']

   zipped = zip(list1, list2)
   print(list(zipped))
   # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
   ```

2. **Different Length Iterables**

   ```python
   list1 = [1, 2, 3, 4]
   list2 = ['a', 'b']

   zipped = zip(list1, list2)
   print(list(zipped))
   # Output: [(1, 'a'), (2, 'b')]
   ```

3. **Using with More Than Two Iterables**

   ```python
   list1 = [1, 2]
   list2 = ['a', 'b']
   list3 = [True, False]

   zipped = zip(list1, list2, list3)
   print(list(zipped))
   # Output: [(1, 'a', True), (2, 'b', False)]
   ```

4. **Unzipping Using `zip()`**
   If you have a zipped object and want to unzip it back to individual lists, you can use the `*` operator:

   ```python
   zipped = [(1, 'a', True), (2, 'b', False)]

   list1, list2, list3 = zip(*zipped)
   print(list1)  # Output: (1, 2)
   print(list2)  # Output: ('a', 'b')
   print(list3)  # Output: (True, False)
   ```

#### Practical Uses

- **Iterating in Parallel**: When you have two or more lists and you want to iterate over them in parallel.

  ```python
  names = ['Alice', 'Bob', 'Charlie']
  scores = [85, 90, 95]

  for name, score in zip(names, scores):
      print(f"{name} scored {score}")
  # Output:
  # Alice scored 85
  # Bob scored 90
  # Charlie scored 95
  ```

- **Dictionary Creation**: When you want to create a dictionary from two related lists.
  ```python
  keys = ['name', 'age', 'city']
  values = ['Alice', 25, 'New York']

  dictionary = dict(zip(keys, values))
  print(dictionary)
  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
  ```
