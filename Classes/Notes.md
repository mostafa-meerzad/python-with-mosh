# Classes

In Python, classes are a fundamental part of object-oriented programming (OOP). A class defines a blueprint for creating objects (instances), allowing you to bundle data (attributes) and behaviors (methods) together.

## Basic Structure of a Class

Here's a simple example to illustrate the basic structure of a class in Python:

```python
class Dog:
    # Class attribute
    species = 'Canis familiaris'

    # Initializer / Instance Attributes, if the instance object needs initial values
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
```

### Components of a Class

1. **Class Name**: The name of the class (`Dog` in this example).
2. **Class Attribute**: A variable that is shared among all instances of a class. In this case, `species` is a class attribute.
3. **Initializer (`__init__` method)**: The constructor method for a class. It is automatically called when a new instance of the class is created. It initializes the instance attributes.
4. **Instance Attributes**: Variables that are unique to each instance. In this case, `name` and `age` are instance attributes.
5. **Instance Methods**: Functions defined within a class that operate on instances of that class. They typically use `self` to refer to the instance they operate on.
6. methods like this one `__init__` is called magic methods
7. methods defined in a class must at least take one parameter which is `self`.
8. `self` is a reference to the new instance object made by the class, we don't need to manually provide `self` since Python does that by itself.

### Creating Instances

To create an instance of a class, you call the class as if it were a function:

```python
dog1 = Dog('Buddy', 9)
dog2 = Dog('Lucy', 3)
```

### Accessing Attributes and Methods

You can access the attributes and methods of an instance using dot notation:

```python
print(dog1.name)         # Output: Buddy
print(dog1.age)          # Output: 9
print(dog1.species)      # Output: Canis familiaris

print(dog1.description())  # Output: Buddy is 9 years old
print(dog1.speak('Woof'))  # Output: Buddy says Woof
```

## Instance Methods and Attributes

### Instance Methods

Instance methods are the most common type of methods in Python. They operate on an instance of the class, and they can access and modify the instance's attributes. When defining an instance method, you must include `self` as the first parameter, which refers to the specific instance of the class.

Example:

```python
class MyClass:
    def __init__(self, value):
        self.value = value  # Instance attribute

    def instance_method(self):
        return self.value  # Accessing instance attribute
```

Here, `instance_method` is an instance method that can access `self.value`, which is an instance attribute.

### Instance Attributes

Instance attributes are variables that are specific to each instance of a class. They are usually defined within the `__init__` method, which is the initializer method for the class.

Example:

```python
class MyClass:
    def __init__(self, value):
        self.value = value  # Instance attribute
```

Each instance of `MyClass` can have a different value for `self.value`.

## Class Methods and Attributes

### Class Methods

Class methods are methods that are bound to the class and not the instance of the class. They take `cls` as the first parameter, which refers to the class itself. Class methods can access class attributes but not instance attributes. You can define a class method using the `@classmethod` decorator.

Example:

```python
class MyClass:
    class_attribute = 'I am a class attribute'

    @classmethod
    def class_method(cls):
        return cls.class_attribute  # Accessing class attribute
```

Here, `class_method` is a class method that can access `cls.class_attribute`, which is a class attribute.

### Class Attributes

Class attributes are variables that are shared among all instances of a class. They are defined within the class body, but outside any instance methods.

Example:

```python
class MyClass:
    class_attribute = 'I am a class attribute'  # Class attribute
```

All instances of `MyClass` share the same `class_attribute`.

## Differences

1. **Binding**:

   - **Instance Methods**: Bound to an instance of the class. Accessed using the instance (`instance.method()`).
   - **Class Methods**: Bound to the class itself. Accessed using the class (`Class.method()`) or an instance (`instance.method()`), though the latter is less common.

2. **First Parameter**:

   - **Instance Methods**: Take `self` as the first parameter, referring to the instance.
   - **Class Methods**: Take `cls` as the first parameter, referring to the class.

3. **Attributes Access**:
   - **Instance Methods**: Can access both instance attributes and class attributes.
   - **Class Methods**: Can access only class attributes.

### Summary

- **Instance Methods**: Operate on instances; first parameter is `self`.
- **Instance Attributes**: Specific to each instance; defined in `__init__`.
- **Class Methods**: Operate on the class; first parameter is `cls`; defined with `@classmethod`.
- **Class Attributes**: Shared among all instances; defined in the class body.
- **Static Methods**: Do not operate on instance or class; no `self` or `cls`; defined with `@staticmethod`.

Understanding these distinctions helps in designing clean, maintainable, and efficient object-oriented code in Python.

## Class Magic Methods

Magic methods, also known as dunder methods (short for "double underscore"), are special methods in Python that start and end with double underscores. They are used to define how objects of a class behave in different situations, such as when they are added together, compared, or printed. These methods allow custom objects to emulate built-in types and provide a way to implement operator overloading and other special behaviors.

Here are some common categories of magic methods and examples of how they can be used:

### Initialization and Representation

- `__init__(self, ...)`: Called when an instance is created (the initializer).
  
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
  ```

- `__repr__(self)`: Provides the "official" string representation of an object, useful for debugging.
  
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __repr__(self):
          return f"MyClass(value={self.value})"
  ```

- `__str__(self)`: Provides the "informal" or nicely printable string representation of an object.
  
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __str__(self):
          return f"Value: {self.value}"
  ```

### Arithmetic Operations

These methods allow objects to support arithmetic operations like addition, subtraction, multiplication, etc.

- `__add__(self, other)`: Defines behavior for the `+` operator.
  
  ```python
  class MyNumber:
      def __init__(self, value):
          self.value = value
      
      def __add__(self, other):
          return MyNumber(self.value + other.value)
  ```

- `__sub__(self, other)`: Defines behavior for the `-` operator.
  
  ```python
  class MyNumber:
      def __init__(self, value):
          self.value = value
      
      def __sub__(self, other):
          return MyNumber(self.value - other.value)
  ```

- Similar methods exist for other arithmetic operations: `__mul__` (multiplication), `__truediv__` (true division), `__floordiv__` (floor division), `__mod__` (modulus), `__pow__` (exponentiation), etc.

### Comparison Operations

These methods define how objects are compared using operators like `<`, `<=`, `>`, `>=`, `==`, and `!=`.

- `__eq__(self, other)`: Defines behavior for the `==` operator.
  
  ```python
  class MyNumber:
      def __init__(self, value):
          self.value = value
      
      def __eq__(self, other):
          return self.value == other.value
  ```

- `__lt__(self, other)`: Defines behavior for the `<` operator.
  
  ```python
  class MyNumber:
      def __init__(self, value):
          self.value = value
      
      def __lt__(self, other):
          return self.value < other.value
  ```

- Similar methods exist for other comparison operations: `__le__` (less than or equal to), `__gt__` (greater than), `__ge__` (greater than or equal to), `__ne__` (not equal).

### Container Emulation

These methods allow objects to emulate container types like lists or dictionaries.

- `__len__(self)`: Defines behavior for the `len()` function.
  
  ```python
  class MyList:
      def __init__(self, items):
          self.items = items
      
      def __len__(self):
          return len(self.items)
  ```

- `__getitem__(self, key)`: Defines behavior for indexing.
  
  ```python
  class MyList:
      def __init__(self, items):
          self.items = items
      
      def __getitem__(self, index):
          return self.items[index]
  ```

- `__setitem__(self, key, value)`: Defines behavior for setting an item at a specific index.
  
  ```python
  class MyList:
      def __init__(self, items):
          self.items = items
      
      def __setitem__(self, index, value):
          self.items[index] = value
  ```

- `__delitem__(self, key)`: Defines behavior for deleting an item at a specific index.
  
  ```python
  class MyList:
      def __init__(self, items):
          self.items = items
      
      def __delitem__(self, index):
          del self.items[index]
  ```

### Attribute Access

These methods control how attributes are accessed, set, or deleted.

- `__getattr__(self, name)`: Called when trying to access an attribute that doesn't exist.
  
  ```python
  class MyClass:
      def __getattr__(self, name):
          return f"{name} not found"
  ```

- `__setattr__(self, name, value)`: Called when setting an attribute.
  
  ```python
  class MyClass:
      def __setattr__(self, name, value):
          self.__dict__[name] = value
  ```

- `__delattr__(self, name)`: Called when deleting an attribute.
  
  ```python
  class MyClass:
      def __delattr__(self, name):
          del self.__dict__[name]
  ```

### Context Management

These methods allow an object to be used with the `with` statement, providing a way to allocate and release resources.

- `__enter__(self)`: Called when entering the context.
- `__exit__(self, exc_type, exc_value, traceback)`: Called when exiting the context.
  
  ```python
  class MyContextManager:
      def __enter__(self):
          print("Entering context")
          return self
      
      def __exit__(self, exc_type, exc_value, traceback):
          print("Exiting context")
  
  with MyContextManager() as manager:
      print("Inside the context")
  ```

### Summary

Magic methods provide a powerful way to customize the behavior of objects in Python. By defining these methods, you can make your custom objects behave like built-in types, support operator overloading, and integrate seamlessly with Python's language features. Understanding and using magic methods can greatly enhance the flexibility and expressiveness of your code.