# Python

## Intro

Python is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van
Rossum and first released in 1991, Python's design philosophy emphasizes code readability and syntax that allows
programmers to express concepts in fewer lines of code compared to other languages like C++ or Java.

### Key Features of Python:

1. **Simple and Easy to Learn**: Python's syntax is designed to be intuitive and its language constructs make it easy to
   learn, even for beginners.
2. **Versatile**: Python is a general-purpose language used for web development, data analysis, artificial intelligence,
   scientific computing, automation, and more.
3. **Interpreted Language**: Python code is executed line-by-line, which makes debugging easier but can impact
   performance.
4. **Extensive Standard Library**: Python comes with a large standard library that includes modules and packages for
   virtually every task, from file I/O to web development.
5. **Cross-Platform**: Python is available on multiple operating systems including Windows, macOS, and Linux, which
   allows for cross-platform development.
6. **Community Support**: Python has a large and active community, contributing to a wealth of third-party modules and
   tools, as well as extensive documentation and tutorials.

### Common Use Cases:

- **Web Development**: Frameworks like Django and Flask make Python a popular choice for backend web development.
- **Data Science and Machine Learning**: Libraries such as Pandas, NumPy, and Scikit-learn are widely used in data
  analysis and machine learning.
- **Automation**: Python's simplicity and readability make it an excellent choice for scripting and automating
  repetitive tasks.
- **Software Development**: Python is used in developing desktop applications, game development, and even network
  servers.

Python's combination of simplicity, versatility, and a strong support community has made it one of the most popular
programming languages in the world.

## Python implementation and specification

Python has several implementations, each catering to different use cases and performance needs. Here’s an overview of
the most notable implementations and the official specification that guides them:

### Major Python Implementations

1. **CPython**:

   - **Description**: The reference implementation of Python, written in C.
   - **Features**:
     - Most widely used implementation.
     - Compiles Python code to intermediate bytecode, which is then interpreted by a virtual machine.
     - Extensive standard library and wide support for third-party libraries.
   - **Use Cases**: General-purpose programming, web development, scientific computing, and more.

2. **PyPy**:

   - **Description**: An alternative implementation of Python, focusing on speed and efficiency.
   - **Features**:
     - Just-In-Time (JIT) compiler that translates Python code to machine code at runtime, offering significant speed
       improvements for many workloads.
     - Compatible with the majority of Python code.
   - **Use Cases**: Applications requiring high performance, such as numerical computations and long-running processes.

3. **Jython**:

   - **Description**: Implementation of Python designed to run on the Java platform.
   - **Features**:
     - Translates Python code into Java bytecode, which can be executed on the Java Virtual Machine (JVM).
     - Allows seamless integration with Java libraries and applications.
   - **Use Cases**: Projects that need to interact with Java codebases or run within Java environments.

4. **IronPython**:

   - **Description**: Implementation of Python for the .NET framework.
   - **Features**:
     - Translates Python code into .NET Intermediate Language (IL), which can be executed by the Common Language
       Runtime (CLR).
     - Integrates with .NET libraries and services.
   - **Use Cases**: Applications that need to leverage .NET infrastructure or interact with other .NET languages.

5. **MicroPython**:
   - **Description**: A lean and efficient implementation of Python for microcontrollers and embedded systems.
   - **Features**:
     - Designed to run with limited resources.
     - Supports a subset of the Python standard library tailored for embedded development.
   - **Use Cases**: Embedded systems, Internet of Things (IoT) projects, and other resource-constrained environments.

### Python Language Specification

The Python language specification is outlined in the Python Enhancement Proposals (PEPs), which are documents that
describe new features, processes, and information about the Python language. Key PEPs include:

1. **PEP 8**:

   - **Title**: Style Guide for Python Code
   - **Content**: Provides conventions for writing readable and maintainable Python code, including naming conventions,
     indentation, and more.

2. **PEP 20**:

   - **Title**: The Zen of Python
   - **Content**: A collection of aphorisms that capture the philosophy of Python, emphasizing simplicity, readability,
     and the importance of writing explicit code.

3. **PEP 484**:

   - **Title**: Type Hints
   - **Content**: Introduces optional type hinting to Python, enabling static type checking and better code clarity
     without changing the runtime behavior.

4. **PEP 257**:
   - **Title**: Docstring Conventions
   - **Content**: Guidelines for writing docstrings in Python, including conventions for formatting and content.

### Conclusion

The various implementations of Python cater to different needs, whether it's performance optimization with PyPy,
integration with Java via Jython, or embedded systems development with MicroPython. The language specification,
primarily driven by PEPs, ensures that Python maintains consistency, readability, and a coherent philosophy across its
implementations.

## Variables

Defining variables in python is very easy

```py
name = "Mostafa"
age = 23
height = 175.5
married = False

```

assigning the same value to multiple variables

```py
a = b = c = 19
```

assigning multiple variable in the same line

```py
a, b = 1, 5
```

### Type Annotation

Python is a **dynamic-typed language** which means variable types are determined at **run time** unlike **static-typed
languages** which types are determined at **compile time**.

in python changing variable's value to completely different types

```py

name = "Mostafa"
# then somewhere in the program you change value of name to something completely different
name = 100

```

from **python 3.6** we can annotate variable types

```py
name: str = "Mostafa"
age: int = 23
```

### Mutable and Immutable Types

`id()` is a global function which returns the memory location allocated for the specified identifier

```py

x = 1

print(id(x))  # => 1384214063408

x = x + 1

print(id(x))  # => 1384214063440

nums = [1, 2, 4]
print(id(nums))  # => 2331135203072

nums.append(10)
print(id(nums))  # => 2331135203072

```

## Strings

Strings are immutable data-types

`len()` is a global function which returns the number of character of a string or number of elements in a list

```py
course = "Python Programming"
print(len(course))  # 18 => number of characters in the string
print(course[0])  # p => first character of string
print(course[-1])  # g => first element form the end of the string
print(course[0:3])  # pyt => a slice of string starting from 0 (first element) to 3 (fourth element but except itself)
print(course[:])  # Python Programming => from first to last element or the whole string
print(course[:2])  # Pyt =>starting point omitted 0 used as default value
print(course[4:])  # on Programming => ending point omitted len(course) used as default value

# strings are immutable therefore new memory is located for each string operation
print(id(course))  # 1345471682240
print(id(course[0]))  # 1345471658224
```

### Scape Sequences

`\'`
`\"`
`\n`
`\t`
`\\`

### Formatted Strings

formatted string unlike string literal isn't a value instead is an expression which will evaluate at run-time

`F""`, `f""`, `f''` and `F''` are all the same and represent a formatted-string

`{}` are used within formatted-strings to include a dynamic value or in general we can put any valid expression
within `{}`

```py

first = "Mostafa"
last = "Meerzad"
full = first + " " + last  # string concatenation

full = f"{first} {last}"  # formatted string
full = F"{first} {last}"  # formatted string

print(full)
print(f"this is the length of fullName {len(full)}")
```

### String Methods

```py
course = " Python Programming on"

print(course.upper())  # returns a copy of the string turned into uppercase
print(course.lower())  # returns a copy of the string turned into lowercase
print(course.split(" "))  # returns a list of parts of the string separated with the provided separator
print(course.strip())  # returns a copy of string with leading and trailing whitespaces removed
print(course.rstrip())  # stript right
print(course.lstrip())  # strip left
print(course.count("on", 0, 9))  # Return the number of non-overlapping occurrences of substring sub in string
print(course.count("m"))
print(course.casefold())  # removes casing, useful for comparison
print(course.istitle())  # True if string is titleCase
print(course.islower())
print(course.isupper())
print(course.isalnum())  # True if string is alphanumeric (mix of letters and numbers)

print(course.find("Pro"))  # returns the starting index of substring -1 if non existing
print(course.replace(" ", "#"))  # reruns a copy of string with characters replaced

print("Programming" in course)  # use in operator to check if substring is included in the string
print("Python" not in course)  # not operator also exist to negate

```

## Numbers

```py
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

```

### Arithmetic Operations

```py
a = 1 + 2
a = 1 - 2
a = 1 * 2
a = 1 / 2  # floating-point division
a = 1 // 2  #
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
```

**Note**: in python unlike other programming languages we don't have _increment_ or _decrement_ operators like `x++`
or `x--`

### Working with Numbers

```py
import math

x = 3.49
print(math.floor(x))
print(math.ceil(x))
print(round(x))
print(abs(x))
print(math.pi)
```

## Type Conversion

Python is a strongly-typed language which means it doesn't perform type conversions on it's own and type conversion is
our responsibility, unlike languages like javascript that is loosely-typed language which performs type-conversion
without explicitly saying to.

Sometimes we need to convert types from one to another, here are functions used for type-conversion

`str(val)` converts val to string, `int(val)` converts val to integer, `bool(val)` coverts val to boolean, `float(val)`
converts val to floating-point,

**Falsy values**:
**False**, **""**, **[]**, **0** and **None**

**any value that is not falsy is truthy**

## Conditional Statements

In python we don't have parenthesis or curly-braces for conditional statements just **indentation**

```py
age = 24

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("All done!")

```

if you need to have an empty block use **pass** keyword

```py
if x > 1:
    pass
else:
    pass
```

## Logical Operators

`and`, `or` and `not` are logical operators

```py

# name = "John"
name = ""

# name = " "  # " " a string with just one space is not considered an empty string
# if not name.strip(): # solution is to strip the white-spaces

if not name.strip():
    print("name is empty")

age = 19

if age >= 18 and age < 65:
    print("Eligible")

# the same comparison as above
if 18 <= age < 65:  # this is called chaining comparison-operators
    print("Eligible")

```

## Ternary Operator

```py
age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)
```

same statement with ternary-operator in python way

```py

age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

```

## Loops

### for loop

we can iterate over any object that is iterable

```py
# iterating over characters of an string
for x in "Mostafa":
    print(x)

# iterating over each elements of a list
for x in ["a", "b", "c"]:
    print(x)

# iterating over a sequence of numbers
for x in range(10):
    print(x)
```

`range(start, end, step)` range function is used to create an iterable sequence of numbers, range function returns a \*
\*range object\*\*, range-objects take very little amount of memory unlike lists that take a lot of memory in case of
really large objects.

range object generates one element for each iteration instead of creating all elements at once!

```py
range(5000000)  # -> range object

[list,
with , 5000000, elements]  # -> takes very large space
```

```py
for x in range(2, 10, 2):
    print(x)
```

#### For...Else

Consider a scenario that you have a list of names and want to find the first name matching our criteria and immediately
jump out of the loop (for performance reasons) display a message if no matching name found

```py
 names = ["John", "Mary"]

found = False
for name in names:
    if name.startswith("J"):
        print("Name Found")
        found = True
        break
if not found:
    print("Name not found")
```

```py
 names = ["John", "Mary"]

# for...else
# else block is executed if our for-loop completes successfully without an immediate break
for name in names:
    if name.startswith("J"):
        print("Name Found")
        found = True
        break
else:
    print("Name not found")

```

### while loop

```py
guess = 0
answer = 5

while guess != answer:
    guess = int(input("Guess: "))

```

```py
guess = 0
answer = 5

# while...else
# else block is executed if our while-loop completes successfully without an immediate break
while guess != answer:
    guess = int(input("guess: "))
    if guess == 1000:
        print("you did guess the king number")
        break

else:
    print("you didn't guess the king number but guessed the correct answer")

```

## Functions

```py
def functionName(parameters):
    # function block
    # statements
    # statements
    # statements
    # ...
    return values  # return one value
    return (val1, val2, vals...)  # return a tuple (like a read only list) of values


functionName(args)
```

**Note**:

1. **default return value**: returned from functions is **None**
2. **keyword arguments**: when you need to explicitly assign a value to a function
   argument `function(firstArg=value, arg, arg)`

```py
def increment(number, by):
    print("incrementing...")
    return number + by
    return (number, by, number + by)


print(increment(100, by=2))
```

3. **assigning default value to a function-parameter**

```py
def increment(number, by=10):
    print("incrementing...")
    return number + by
    return (number, by, number + by)


print(increment(100))  # by argument is not specified
print(increment(100, 2))  # by argument is specified
```

4. **type annotation**

```py
#            number: type, by: type   -> return type :
def increment(number: int, by: int = 10) -> int:
    print("incrementing...")
    return number + by


def increment(number: int, by: int = 10) -> tuple:
    print("incrementing...")
    return (number, number + by)
```

### \*args, arguments

when you need to pass an arbitrary number of arguments to a function use can use `def functionName(*args)`
`*args` return a tuple of all passed arguments to the function which we can iterate over

```py

def myFunction(*args):
    printargs  # this return a tuple of arguments
    for x in args:
        print(x)


myFunction(1, 2, 3, 5, 6, 7)
```

### \*\*args, keyword arguments

if we need to pass an arbitrary number of keyword-arguments to a function use `def functionName(**kwarg)`
`**kwargs` return a dictionary of all keyword-arguments

```pycon

def saveUser(**kwargs):
    kwargs # returns a dictionary of provided keyword-arguments
    print(kwargs)

```

## Variable Scopes

In Python we have two types of variables:

1. file level variables:
   variables defined in file scope which are also called global variables are visible/accessible to all the functions
   inside the file
2. function level variables:
   variables defined inside functions are only visible/accessible inside those functions

variables in python are not block level unlike other programming languages which means variables defined inside a
block of code is accessible to the outside scope as well

```python
message = "global message"  # a global variable


def greet():
    # accessing global message variable before making it a local variable
    print(message)  # message still shows global value 'global message'

    # if you assign global variable another value in this function block
    # like so
    message = "new message"
    # python will create another local variable with the same name 'message' and assign it the new value
    # doing so has no effect on the global value

    print(message)  # message is now a local variable and has 'new message'


print(message)  # message is 'global message'

def sayHi():
    # block level variables are accessible throughout the function
    message = "Hello" # function level variable

    if True:
        print(message)
        other = "CONDITIONAL" # var defined inside code-block

    for x in [1,2]:
        print(x)
        print(message)
        another = "LOOP" # var defined inside loop body

    print("var defined in conditional statement ", other)
    print("var defined in loop ", another)
    print("var defined in function ", message)

sayHi()

```

changing value of a global variable

```python

def sayHi():
    # if you need to change the value of a global variable here is how
    global message
    message = "Hello global" # function level variable

    if True:
        print(message)
        other = "CONDITIONAL" # var defined inside code-block

    for x in [1,2]:
        print(x)
        print(message)
        another = "LOOP" # var defined inside loop body

    print("var defined in conditional statement ", other)
    print("var defined in loop ", another)
    print("var defined in function ", message)

sayHi()

```

**Note**: avoid using/modifying global variables because there might be other functions and parts of code relying on the value of it, this is a bad practice!
