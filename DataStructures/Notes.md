# Data Structures

## List

Lists in Python are a versatile and widely-used data structure that allow you to store collections of items. Here are the key characteristics and functionalities of lists:

### Characteristics of Lists

1. **Ordered**: The items in a list are ordered. This means that each item has a specific position within the list, and this position does not change unless you explicitly modify the list.
2. **Mutable**: Unlike tuples, lists are mutable, meaning you can change their content by adding, removing, or modifying elements.
3. **Dynamic**: Lists can grow and shrink as needed, accommodating any number of elements.
4. **Heterogeneous**: Lists can contain elements of different data types, including other lists.

### Creating Lists

You can create lists using square brackets `[]` or the `list()` constructor:

- **Using square brackets**:

  ```python
  my_list = [1, 2, 3]
  ```

- **Using the `list()` function**:

  ```python
  my_list = list((1, 2, 3))
  ```

- **Creating an empty list**:
  ```python
  empty_list = []
  empty_list = list()
  ```

### Accessing List Elements

You can access elements in a list using indexing, similar to arrays in other programming languages:

- **Indexing**:

  ```python
  my_list = [1, 2, 3]
  print(my_list[0])  # Output: 1
  print(my_list[1])  # Output: 2
  print(my_list[2])  # Output: 3
  ```

- **Negative indexing**:

  ```python
  print(my_list[-1])  # Output: 3
  print(my_list[-2])  # Output: 2
  print(my_list[-3])  # Output: 1
  ```

- **Slicing**:
  ```python
  print(my_list[0:2])  # Output: [1, 2]
  print(my_list[:2])   # Output: [1, 2]
  print(my_list[1:])   # Output: [2, 3]
  print(my_list[:])    # Output: [1, 2, 3]
  ```

### Modifying Lists

Lists can be modified in several ways:

- **Adding elements**:

  ```python
  my_list.append(4)        # Adds 4 to the end of the list
  my_list.insert(1, 1.5)   # Inserts 1.5 at index 1
  ```

- **Removing elements**:

  ```python
  my_list.remove(1)        # Removes the first occurrence of 1
  removed_item = my_list.pop(1)  # Removes and returns the item at index 1
  last_item = my_list.pop()      # Removes and returns the last item
  my_list.clear()          # Removes all elements
  ```

- **Modifying elements**:
  ```python
  my_list[0] = 10          # Changes the first element to 10
  my_list[1:3] = [20, 30]  # Changes elements at index 1 and 2
  ```

### List Operations

Lists support various operations:

- **Concatenation**:

  ```python
  list1 = [1, 2, 3]
  list2 = [4, 5, 6]
  combined = list1 + list2  # Output: [1, 2, 3, 4, 5, 6]
  ```

- **Repetition**:

  ```python
  repeated = list1 * 2      # Output: [1, 2, 3, 1, 2, 3]
  ```

- **Checking membership**:
  ```python
  is_in_list = 2 in list1   # Output: True
  ```

### List Comprehensions

List comprehensions provide a concise way to create lists:

```python
squares = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]
```

### Common List Methods

- `append(item)`: Adds an item to the end of the list.
- `extend(iterable)`: Extends the list by appending all the items from the iterable.
- `insert(index, item)`: Inserts an item at a given position.
- `remove(item)`: Removes the first occurrence of an item.
- `pop([index])`: Removes and returns the item at the given position (last item if index is not provided).
- `clear()`: Removes all items from the list.
- `index(item, [start], [end])`: Returns the index of the first occurrence of the item.
- `count(item)`: Returns the number of occurrences of the item.
- `sort([key], [reverse])`: Sorts the items of the list in place.
- `reverse()`: Reverses the elements of the list in place.
- `copy()`: Returns a shallow copy of the list.

### Use Cases of Lists

1. **Dynamic Data Storage**: Suitable for collections of items that may change in size.
2. **Iteration and Filtering**: Useful for loops and comprehensions.
3. **Homogeneous and Heterogeneous Data**: Can store elements of the same type or different types.

### Summary

Lists in Python are a powerful and flexible data structure that can store ordered collections of items. They support a wide range of operations, including modification, iteration, and sorting, making them an essential tool for many programming tasks.

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

`listName[0]` returns the very-first element

accessing an element outside the list range throws an `IndexError`

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

## Stack

In Python, stacks can be represented using various data structures such as lists or using the `collections.deque` class. Below, we'll discuss both approaches and provide examples.

### Using Lists as Stacks

The simplest way to implement a stack in Python is by using a list. Lists provide the `append()` method to add items to the stack and the `pop()` method to remove items from the stack, both of which operate in O(1) time.

Here is an example:

```python
# Using list as a stack
stack = []

# Push items onto the stack
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack:")
print(stack)

# Pop items from the stack
print("\nElements popped from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after removing elements:")
print(stack)

# Empty stack truthy check
if not stack:
    print("stack is empty!")
```

### Using `collections.deque` as a Stack

While lists are straightforward for stack operations, the `collections.deque` class can also be used. The `deque` class provides an efficient and thread-safe way to perform append and pop operations from both ends. However, for a stack, we'll only use the right end.

Here is an example using `deque`:

```python
from collections import deque

# Initialize a deque
stack = deque()

# Push items onto the stack
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack:")
print(stack)

# Pop items from the stack
print("\nElements popped from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after removing elements:")
print(stack)
```

### Explanation of Stack Operations

- **Push Operation**: Add an element to the top of the stack.

  - For lists: `stack.append(item)`
  - For `deque`: `stack.append(item)`

- **Pop Operation**: Remove and return the top element of the stack.

  - For lists: `stack.pop()`
  - For `deque`: `stack.pop()`

- **Peek Operation**: Return the top element without removing it (not directly available in `deque` but can be achieved by accessing the last element).
  - For lists: `stack[-1]`
  - For `deque`: `stack[-1]`

### Example with Peek Operation

Here's how you can implement a peek operation in both list-based and deque-based stacks:

#### List-based Stack with Peek

```python
# Using list as a stack with peek
stack = []

# Push items onto the stack
stack.append('a')
stack.append('b')
stack.append('c')

# Peek at the top item
top_item = stack[-1]
print("Top item (peek):", top_item)

# Pop items from the stack
stack.pop()
stack.pop()
stack.pop()
```

#### Deque-based Stack with Peek

```python
from collections import deque

# Initialize a deque
stack = deque()

# Push items onto the stack
stack.append('a')
stack.append('b')
stack.append('c')

# Peek at the top item
top_item = stack[-1]
print("Top item (peek):", top_item)

# Pop items from the stack
stack.pop()
stack.pop()
stack.pop()
```

### Summary

- **Lists** are simple and efficient for implementing stacks in Python using `append()` and `pop()` methods.
- **`collections.deque`** provides a thread-safe and efficient way to implement stacks, with O(1) operations for appending and popping elements from the right end.
- Both approaches allow you to perform typical stack operations like push, pop, and peek effectively.

## Queues

In Python, queues can be represented using various built-in data structures such as lists or using modules that provide more efficient implementations for queue operations. One such module is the `collections` module, which includes the `deque` class.

### Using Lists as Queues

You can use a Python list to implement a queue, where you can add items to the end and remove items from the front. Here's a basic example:

```python
# Using list as a queue
queue = []

# Enqueue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Dequeue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
```

While this approach works, it is not the most efficient because removing elements from the front of the list (using `pop(0)`) requires shifting all the remaining elements, which is an O(n) operation.

### Using `collections.deque`

The `collections.deque` (double-ended queue) class is a more efficient way to implement queues in Python. It provides an O(1) time complexity for append and pop operations from both ends of the deque.

#### Basic Operations

Here's how to use `collections.deque` to implement a queue:

```python
from collections import deque

# Initialize a deque
queue = deque()

# Enqueue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Dequeue
print("\nElements dequeued from the queue")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("\nQueue after removing elements")
print(queue)
```

#### Explanation of `deque` methods

- `append(x)`: Adds `x` to the right end of the deque.
- `appendleft(x)`: Adds `x` to the left end of the deque.
- `pop()`: Removes and returns an element from the right end of the deque. Raises an `IndexError` if the deque is empty.
- `popleft()`: Removes and returns an element from the left end of the deque. Raises an `IndexError` if the deque is empty.
- `extend(iterable)`: Extends the right side of the deque by appending elements from the iterable.
- `extendleft(iterable)`: Extends the left side of the deque by appending elements from the iterable (note that the order of elements is reversed).
- `rotate(n)`: Rotates the deque n steps to the right. If n is negative, it rotates to the left.
- `maxlen`: When provided, it sets the maximum length of the deque. Once the deque reaches the maximum length, any new elements added will discard elements from the opposite end.

### Example of a Bounded `deque`

You can also create a deque with a maximum length. This is useful for implementing fixed-size queues or buffers.

```python
# Initialize a deque with a maximum length
bounded_queue = deque(maxlen=3)

# Enqueue
bounded_queue.append('a')
bounded_queue.append('b')
bounded_queue.append('c')
print("Bounded queue after adding 3 elements:")
print(bounded_queue)

# Adding another element will discard the leftmost one
bounded_queue.append('d')
print("Bounded queue after adding another element:")
print(bounded_queue)
```

In this example, the maximum length of the deque is 3. When a fourth element is added, the leftmost element is discarded to make space for the new one.

### Summary

- Lists can be used to implement queues but are less efficient for dequeue operations.
- The `collections.deque` class is optimized for queue operations, providing O(1) time complexity for append and pop operations from both ends.
- `deque` supports various methods that allow you to manipulate the queue efficiently, and it can be bounded to limit its maximum size.

#### How rotate(n) Works

- Positive n: When n is positive, the rotation moves elements from the end of the deque to the beginning. Each element is shifted to the right by n positions.
- Negative n: When n is negative, the rotation moves elements from the beginning of the deque to the end. Each element is shifted to the left by |n| positions.

Here's a detailed example to illustrate how rotate(n) works:

##### Example with rotate(n)

Initializing a `Deque`

```python
from collections import deque

# Initialize a deque with some elements
dq = deque(['a', 'b', 'c', 'd', 'e'])

print("Initial deque:")
print(dq)
```

Rotating to the Right (Positive n)

```python
# Rotate the deque to the right by 2 steps
dq.rotate(2)

print("\nDeque after rotating to the right by 2 steps:")
print(dq)
```

Explanation: The last two elements `d` and `e` move to the front, resulting in `deque(['d', 'e', 'a', 'b', 'c'])`.

```python
# Rotate the deque to the left by 3 steps
dq.rotate(-3)

print("\nDeque after rotating to the left by 3 steps:")
print(dq)
```

## Tuples

Tuples in Python are a type of data structure that can store a sequence of values. They are similar to lists but have a few key differences:

1. **Immutability**: Once a tuple is created, its contents cannot be changed. This means you cannot add, remove, or modify elements in a tuple after it is created. This immutability makes tuples useful for storing data that should not be modified.

2. **Syntax**: Tuples are defined using parentheses `()` whereas lists use square brackets `[]`. For example:

   ```python
   my_tuple = (1, 2, 3)
   my_list = [1, 2, 3]
   ```

3. **Usage**: Tuples are often used to group related data. For example, a function that returns multiple values can return them as a tuple. Tuples can also be used as keys in dictionaries because they are immutable.

### Creating Tuples

Tuples can be created in several ways:

- **Using parentheses**:

  ```python
  my_tuple = (1, 2, 3)
  ```

- **Without parentheses (implicit creation)**:

  ```python
  my_tuple = 1, 2, 3
  ```

- **Single element tuple (note the comma)**:

  ```python
  single_element_tuple = (1,)
  ```

- **Using the `tuple()` function**:
  ```python
  my_tuple = tuple([1, 2, 3])
  ```

### Accessing Tuple Elements

Elements in a tuple can be accessed using indexing, similar to lists:

```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2
print(my_tuple[2])  # Output: 3
```

### Tuple Operations

While you cannot modify a tuple, you can perform operations such as concatenation and repetition:

- **Concatenation**:

  ```python
  tuple1 = (1, 2, 3)
  tuple2 = (4, 5, 6)
  combined = tuple1 + tuple2
  print(combined)  # Output: (1, 2, 3, 4, 5, 6)
  ```

- **Repetition**:
  ```python
  my_tuple = (1, 2, 3)
  repeated = my_tuple * 2
  print(repeated)  # Output: (1, 2, 3, 1, 2, 3)
  ```

### Tuple Unpacking

Tuples allow for easy unpacking of values:

```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

### Use Cases of Tuples

1. **Returning Multiple Values from Functions**:

   ```python
   def get_coordinates():
       return (10, 20)

   x, y = get_coordinates()
   ```

2. **Immutable Data Storage**: When you need a collection of items that should not change.

3. **Dictionary Keys**: Tuples can be used as keys in dictionaries because they are immutable.
   ```python
   my_dict = {(1, 2): 'value'}
   ```

### Advantages of Tuples

- **Immutability**: Provides data integrity and can be used as keys in dictionaries.
- **Performance**: Tuples can be more memory-efficient and faster than lists due to their immutability.
- **Clarity**: Tuples can make code more readable when used for fixed collections of items.

### Summary

Tuples are a fundamental data structure in Python, ideal for storing immutable collections of items. They offer a clear and efficient way to handle related data, especially when the data should not be modified.

## Swapping Variables

```python

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

```

under the hood we're defining and unpacking a tuple `x, y = y, x` and `x, y = (y, x)` are the same

## Arrays

In Python, arrays are similar to lists, but they are more efficient for numerical operations and are often used in scientific computing and data analysis. There are different types of arrays in Python, the most common being arrays provided by the `array` module and NumPy arrays from the NumPy library. Here, we'll explain both:

### Arrays Using the `array` Module

The `array` module in Python provides a basic array data structure that can store elements of a single data type.

#### Characteristics

1. **Type Constraint**: Elements must be of the same type, specified at array creation.
2. **Efficiency**: More memory-efficient than lists for large amounts of numerical data.

#### Creating Arrays

You can create arrays using the `array` module by specifying a type code and an initializer list. The type code defines the data type of the array elements.

- **Importing the array module**:

  ```python
  import array
  ```

- **Type Codes**:

  - `'b'`: signed integer (1 byte)
  - `'B'`: unsigned integer (1 byte)
  - `'u'`: Unicode character (2 bytes)
  - `'h'`: signed integer (2 bytes)
  - `'H'`: unsigned integer (2 bytes)
  - `'i'`: signed integer (2 bytes)
  - `'I'`: unsigned integer (2 bytes)
  - `'l'`: signed integer (4 bytes)
  - `'L'`: unsigned integer (4 bytes)
  - `'f'`: floating point (4 bytes)
  - `'d'`: floating point (8 bytes)

- **Creating an array**:
  ```python
  arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' stands for signed integer
  ```

#### Accessing and Modifying Elements

You can access and modify elements using indexing:

```python
print(arr[0])  # Output: 1
arr[1] = 7
print(arr)  # Output: array('i', [1, 7, 3, 4, 5])
```

#### Array Methods

- **Append an element**:

  ```python
  arr.append(6)
  ```

- **Extend with a list of elements**:

  ```python
  arr.extend([7, 8, 9])
  ```

- **Insert an element**:

  ```python
  arr.insert(2, 10)  # Insert 10 at index 2
  ```

- **Remove an element**:

  ```python
  arr.remove(10)
  ```

- **Pop an element**:
  ```python
  arr.pop()  # Removes the last element
  ```

### Arrays Using NumPy

NumPy is a powerful library for numerical computing in Python. It provides the `ndarray` object, which is a more versatile and efficient array than the one provided by the `array` module.

#### Characteristics

1. **Multidimensional**: Supports multi-dimensional arrays.
2. **Vectorized Operations**: Allows for efficient element-wise operations.
3. **Numerical Methods**: Provides a wide range of mathematical functions and operations.

#### Creating NumPy Arrays

You can create NumPy arrays using the `numpy` library:

- **Importing NumPy**:

  ```python
  import numpy as np
  ```

- **Creating an array**:

  ```python
  arr = np.array([1, 2, 3, 4, 5])
  ```

- **Creating arrays with specific values**:
  ```python
  zeros = np.zeros(5)        # Array of zeros
  ones = np.ones((2, 3))     # 2x3 array of ones
  empty = np.empty(4)        # Array with uninitialized values
  arange = np.arange(10)     # Array with values from 0 to 9
  linspace = np.linspace(0, 1, 5)  # Array with 5 values from 0 to 1
  ```

#### Accessing and Modifying Elements

You can access and modify elements using indexing and slicing:

```python
print(arr[0])  # Output: 1
arr[1] = 7
print(arr)  # Output: [1 7 3 4 5]
```

#### Array Operations

NumPy supports a variety of operations:

- **Element-wise operations**:

  ```python
  arr = np.array([1, 2, 3, 4, 5])
  arr = arr + 1  # Output: [2 3 4 5 6]
  arr = arr * 2  # Output: [2 4 6 8 10]
  ```

- **Matrix operations**:

  ```python
  mat1 = np.array([[1, 2], [3, 4]])
  mat2 = np.array([[5, 6], [7, 8]])
  result = mat1.dot(mat2)  # Matrix multiplication
  ```

- **Statistical operations**:
  ```python
  np.mean(arr)  # Mean of the array
  np.sum(arr)   # Sum of the array
  np.max(arr)   # Maximum value in the array
  ```

### Summary

- **Array Module**: Provides basic arrays with a single data type, useful for simple numerical data storage.
- **NumPy Arrays**: Offers advanced, multi-dimensional arrays with a wide range of mathematical operations, ideal for scientific computing and data analysis.

Both types of arrays have their use cases, with NumPy arrays being the preferred choice for more complex and efficient numerical operations.

## Sets

Sets in Python are an unordered collection of unique elements. They are commonly used for membership testing, removing duplicates from a sequence, and mathematical operations like union, intersection, and difference.

### Characteristics of Sets

1. **Unordered**: Sets do not maintain any order for the elements. The items have no index.
2. **Unique Elements**: A set automatically ensures that all elements are unique. If duplicates are added, they are ignored.
3. **Mutable**: Sets themselves are mutable; you can add or remove elements. However, the elements within a set must be immutable (e.g., strings, numbers, tuples).

### Creating Sets

You can create sets using curly braces `{}` or the `set()` function:

- **Using curly braces**:

  ```python
  my_set = {1, 2, 3}
  ```

- **Using the `set()` function**:

  ```python
  my_set = set([1, 2, 3])
  ```

- **Creating an empty set** (Note: `{}` creates an empty dictionary):
  ```python
  empty_set = set()
  ```

### Adding and Removing Elements

You can modify sets by adding or removing elements:

- **Adding elements**:

  ```python
  my_set.add(4)  # Adds a single element
  my_set.update([5, 6])  # Adds multiple elements
  ```

- **Removing elements**:
  ```python
  my_set.remove(2)  # Removes an element; raises KeyError if not found
  my_set.discard(3)  # Removes an element; does nothing if not found
  removed_element = my_set.pop()  # Removes and returns an arbitrary element
  my_set.clear()  # Removes all elements
  ```

### Set Operations

Sets support a variety of operations, including union, intersection, difference, and symmetric difference:

- **Union**: Combines elements from both sets.

  ```python
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
  union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5}
  ```

- **Intersection**: Returns elements common to both sets.

  ```python
  intersection_set = set1 & set2  # Output: {3}
  intersection_set = set1.intersection(set2)  # Output: {3}
  ```

- **Difference**: Returns elements in the first set but not in the second.

  ```python
  difference_set = set1 - set2  # Output: {1, 2}
  difference_set = set1.difference(set2)  # Output: {1, 2}
  ```

- **Symmetric Difference**: Returns elements in either set but not in both.
  ```python
  sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}
  sym_diff_set = set1.symmetric_difference(set2)  # Output: {1, 2, 4, 5}
  ```

### Membership Testing

Sets are optimized for membership testing. It is very efficient to check if an element is in a set:

```python
if 2 in set1:
    print("2 is in the set")
```

### Iterating Through a Set

You can iterate through a set using a loop:

```python
for element in set1:
    print(element)
```

### Set Comprehensions

Similar to list comprehensions, you can create sets using set comprehensions:

```python
squared_set = {x**2 for x in range(5)}  # Output: {0, 1, 4, 9, 16}
```

### Frozensets

A frozenset is an immutable version of a set. You can create a frozenset using the `frozenset()` function:

```python
my_frozenset = frozenset([1, 2, 3])
```

Frozensets can be used as dictionary keys or elements of other sets because they are immutable.

### Common Set Methods

- `add(element)`: Adds an element to the set.
- `remove(element)`: Removes an element from the set; raises KeyError if not found.
- `discard(element)`: Removes an element from the set if it is a member; does nothing if not found.
- `pop()`: Removes and returns an arbitrary element from the set.
- `clear()`: Removes all elements from the set.
- `union(set2)`: Returns the union of two sets.
- `intersection(set2)`: Returns the intersection of two sets.
- `difference(set2)`: Returns the difference of two sets.
- `symmetric_difference(set2)`: Returns the symmetric difference of two sets.

### Use Cases of Sets

1. **Removing Duplicates**: Converting a list to a set removes duplicates.

   ```python
   my_list = [1, 2, 2, 3, 4, 4]
   my_set = set(my_list)  # Output: {1, 2, 3, 4}
   ```

2. **Membership Testing**: Checking if an item is part of a collection.

   ```python
   if 'apple' in my_set:
       print("Apple is in the set")
   ```

3. **Mathematical Set Operations**: Performing union, intersection, and difference operations.

### Summary

Sets in Python are a powerful tool for storing unique elements and performing membership tests and set operations. Their unique characteristics make them suitable for tasks that involve the manipulation and comparison of large collections of data.

## Dictionaries

Dictionaries in Python are a type of data structure that store key-value pairs. They are also known as associative arrays or hash maps in other programming languages. Dictionaries are highly efficient for retrieving, adding, and deleting values based on their keys.

### Characteristics of Dictionaries

1. **Unordered**: Prior to Python 3.7, dictionaries were unordered collections. From Python 3.7 onwards, dictionaries maintain the order of items as they were added.
2. **Mutable**: You can change dictionaries by adding, modifying, or removing key-value pairs.
3. **Keys Must Be Immutable**: Keys in a dictionary must be of an immutable data type, such as strings, numbers, or tuples.
4. **Unique Keys**: Each key in a dictionary must be unique.

### Creating Dictionaries

You can create dictionaries in several ways:

- **Using curly braces**:

  ```python
  my_dict = {"name": "Alice", "age": 25, "city": "New York"}
  ```

- **Using the `dict()` constructor**:

  ```python
  my_dict = dict(name="Alice", age=25, city="New York")
  ```

- **Creating an empty dictionary**:
  ```python
  empty_dict = {}
  empty_dict = dict()
  ```

### Accessing Values

You can access values in a dictionary by referring to their keys:

```python
print(my_dict["name"])  # Output: Alice
```

### Modifying Dictionaries

You can add, modify, or remove key-value pairs:

- **Adding or updating key-value pairs**:

  ```python
  my_dict["email"] = "alice@example.com"  # Adds a new key-value pair
  my_dict["age"] = 26  # Updates the value for the key 'age'
  ```

- **Removing key-value pairs**:
  ```python
  del my_dict["city"]  # Removes the key-value pair for 'city'
  email = my_dict.pop("email")  # Removes and returns the value for 'email'
  my_dict.clear()  # Removes all key-value pairs
  ```

### Dictionary Methods

Dictionaries come with several built-in methods for common operations:

- **Getting a value with a default**:

  ```python
  age = my_dict.get("age", 0)  # Returns 0 if 'age' is not found
  ```

- **Checking if a key exists**:

  ```python
  if "name" in my_dict:
      print("Name is present in the dictionary")
  ```

- **Iterating through keys, values, or key-value pairs**:

  ```python
  for key in my_dict:
      print(key)

  for value in my_dict.values():
      print(value)

  for key, value in my_dict.items():
      print(f"{key}: {value}")
  ```

- **Copying a dictionary**:

  ```python
  new_dict = my_dict.copy()
  ```

- **Merging dictionaries**:
  ```python
  other_dict = {"country": "USA"}
  my_dict.update(other_dict)  # Adds key-value pairs from other_dict to my_dict
  ```

### Dictionary Comprehensions

You can create dictionaries using dictionary comprehensions:

```python
squares = {x: x**2 for x in range(5)}  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Nested Dictionaries

Dictionaries can contain other dictionaries, allowing for nested structures:

```python
nested_dict = {
    "name": "Alice",
    "details": {
        "age": 25,
        "city": "New York"
    }
}
print(nested_dict["details"]["age"])  # Output: 25
```

### Common Use Cases

1. **Storing Configurations and Settings**: Dictionaries are often used to store configuration settings and options.
2. **Representing Structured Data**: They are useful for representing data objects with named attributes.
3. **Counting and Grouping**: Useful for counting occurrences of items and grouping items by keys.
   ```python
   word_counts = {}
   for word in ["apple", "banana", "apple"]:
       word_counts[word] = word_counts.get(word, 0) + 1
   ```

### Summary

Dictionaries are a powerful and flexible data structure in Python for storing and managing key-value pairs. They offer efficient data retrieval and are essential for many programming tasks involving structured data and fast lookups.

## Generators

Generators in Python are a type of iterable, like lists or tuples. However, unlike lists, generators do not store their contents in memory; instead, they generate items on the fly, which makes them more memory efficient, especially when dealing with large data sets.

### Characteristics of Generators

1. **Lazy Evaluation**: Generators produce items one at a time and only when needed. This is known as lazy evaluation.
2. **Memory Efficiency**: Since they generate items one at a time, they are more memory efficient compared to lists that store all elements at once.
3. **Single Iteration**: Generators can only be iterated over once. After the generator is exhausted, it cannot be reused or reset.

### Creating Generators

You can create generators in two main ways: using generator functions and generator expressions.

#### Generator Functions

A generator function is defined like a normal function, but instead of returning a value, it uses the `yield` statement to yield a series of values.

- **Defining a generator function**:

  ```python
  def count_up_to(max):
      count = 1
      while count <= max:
          yield count
          count += 1
  ```

- **Using the generator**:
  ```python
  counter = count_up_to(5)
  for num in counter:
      print(num)
  # Output: 1 2 3 4 5
  ```

#### Generator Expressions

Generator expressions are similar to list comprehensions but with parentheses instead of square brackets. They provide a concise way to create generators.

- **Creating a generator expression**:

  ```python
  gen_exp = (x**2 for x in range(10))
  ```

- **Using the generator expression**:
  ```python
  for num in gen_exp:
      print(num)
  # Output: 0 1 4 9 16 25 36 49 64 81
  ```

### Differences Between `yield` and `return`

- **`yield`**: When a function contains `yield`, it becomes a generator function. `yield` pauses the function and saves its state, returning a value to the caller.
- **`return`**: Ends the function's execution and optionally returns a value to the caller. A function with `return` is not a generator.

### Advantages of Generators

1. **Memory Efficiency**: Generators do not store the entire sequence in memory. They generate each value only when needed.
2. **Representing Infinite Sequences**: Generators can represent infinite sequences. For example, the Fibonacci sequence can be implemented using a generator.
3. **Pipelining Generators**: Generators can be pipelined, allowing data to be processed in stages, each stage represented by a generator.

### Example: Fibonacci Generator

Here's an example of a generator that produces Fibonacci numbers:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator
fib = fibonacci()
for _ in range(10):
    print(next(fib))
# Output: 0 1 1 2 3 5 8 13 21 34
```

### Generator Methods

Generators have a few built-in methods that control their execution:

- **`__iter__()`** and **`__next__()`**: Generators are iterators and have these methods implemented. `__next__()` fetches the next item.

  ```python
  gen = (x**2 for x in range(3))
  print(next(gen))  # Output: 0
  print(next(gen))  # Output: 1
  print(next(gen))  # Output: 4
  ```

- **`send(value)`**: Resumes the generator and sends a value that will be used to replace the current `yield` expression.

  ```python
  def generator():
      while True:
          value = yield
          print(f'Received: {value}')

  gen = generator()
  next(gen)           # Prime the generator
  gen.send('Hello')   # Output: Received: Hello
  ```

- **`close()`**: Stops the generator by raising a `GeneratorExit` exception inside the generator function.

  ```python
  gen = (x**2 for x in range(3))
  gen.close()
  ```

- **`throw(type, value=None, traceback=None)`**: Used to raise an exception inside the generator at the `yield` statement.

  ```python
  def generator():
      try:
          yield
      except ValueError:
          print("ValueError raised inside generator")

  gen = generator()
  next(gen)
  gen.throw(ValueError)
  # Output: ValueError raised inside generator
  ```

### Summary

Generators in Python provide a powerful tool for creating iterators that generate values on the fly, making them memory-efficient and suitable for handling large or infinite sequences. They are created using `yield` in functions or generator expressions and offer several methods to control their execution. Generators are essential for writing clean, efficient, and scalable Python code.

## Unpacking Operator

In Python, the unpacking operator (`*` and `**`) allows for the unpacking of iterables (such as lists or tuples) and dictionaries into function arguments or other data structures. Here's a detailed explanation of both unpacking operators:

### Single Asterisk (\*) for Iterables

The single asterisk `*` is used to unpack iterables. This can be useful in various contexts:

#### Function Arguments

You can use `*` to unpack a list or tuple into positional arguments of a function.

```python
def func(a, b, c):
    print(a, b, c)

args = [1, 2, 3]
func(*args)  # This is equivalent to func(1, 2, 3)
```

#### Merging Lists

You can use `*` to merge lists or other iterables.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]
```

#### Variable-Length Argument Lists

When defining a function, you can use `*args` to accept a variable number of positional arguments.

```python
def func(*args):
    for arg in args:
        print(arg)

func(1, 2, 3)  # This will print 1, 2, 3 on separate lines
```

### Double Asterisk (\*\*) for Dictionaries

The double asterisk `**` is used to unpack dictionaries into keyword arguments.

#### Function Arguments

You can use `**` to unpack a dictionary into keyword arguments of a function.

```python
def func(a, b, c):
    print(a, b, c)

kwargs = {'a': 1, 'b': 2, 'c': 3}
func(**kwargs)  # This is equivalent to func(a=1, b=2, c=3)
```

#### Merging Dictionaries

You can use `**` to merge dictionaries.

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

#### Variable-Length Keyword Arguments

When defining a function, you can use `**kwargs` to accept a variable number of keyword arguments.

```python
def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

func(a=1, b=2, c=3)  # This will print each key-value pair
```

### Combining \* and \*\* in Function Calls

You can combine both `*` and `**` in function calls to unpack both iterables and dictionaries.

```python
def func(a, b, c, d):
    print(a, b, c, d)

args = (1, 2)
kwargs = {'c': 3, 'd': 4}
func(*args, **kwargs)  # This is equivalent to func(1, 2, c=3, d=4)
```

### Summary

- `*` is used to unpack iterables into positional arguments or merge iterables.
- `**` is used to unpack dictionaries into keyword arguments or merge dictionaries.
- Both can be used in function definitions to handle variable numbers of positional and keyword arguments, respectively.

These unpacking operators make Python functions flexible and powerful, allowing for more dynamic and concise code.
