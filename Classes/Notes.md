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

## Private Members

In Python, you can create private properties in classes by using a naming convention where you prefix the property name with double underscores (`__`). This tells Python to name-mangle the property, making it less accessible from outside the class. Here’s a step-by-step explanation of how this works:

### 1. **Understanding Private Properties**

- **Public Properties:** Normally, all attributes and methods in Python are public, meaning they can be accessed directly from outside the class.
- **Private Properties:** To create private properties, which are not meant to be accessed or modified directly from outside the class, you prefix the property name with `__`. Python interprets this as a request to make the property private.

### 2. **How Private Properties Work**

- When you prefix a property with `__`, Python internally changes its name to include the class name. This process is called **name mangling**. For example, if you define a private property `__my_property` in a class `MyClass`, Python internally renames it to `_MyClass__my_property`.
- This makes it harder (but not impossible) to access the property from outside the class, as it requires knowledge of the mangled name.

### 3. **Creating Private Properties**

Here’s an example of creating a class with a private property:

```python
class MyClass:
    def __init__(self, value):
        self.__private_property = value  # Private property

    def get_private_property(self):
        return self.__private_property  # Public method to access the private property

    def set_private_property(self, value):
        self.__private_property = value  # Public method to modify the private property

# Usage
obj = MyClass(10)
print(obj.get_private_property())  # Access via a public method
```

In this example:

- `__private_property` is a private property.
- `get_private_property()` and `set_private_property()` are public methods to access and modify the private property.

### 4. **Accessing Private Properties**

- **Inside the Class:** You can access the private property normally within the class using `self.__private_property`.
- **Outside the Class:** Direct access to `obj.__private_property` will raise an `AttributeError` because the property is private.
  However, you can access it using the mangled name like this: `obj._MyClass__private_property`. This bypasses the privacy mechanism, but it's generally not recommended as it breaks the encapsulation principle.

### 5. **Why Use Private Properties?**

- **Encapsulation:** To hide the internal representation of an object and prevent external code from directly modifying it.
- **Control Access:** To control how properties are accessed or modified by providing getter and setter methods.
- **Code Integrity:** To ensure that the object's state is only changed in a controlled manner.

### 6. **Example with Full Code**

```python
class MyClass:
    def __init__(self, value):
        self.__private_property = value

    def get_private_property(self):
        return self.__private_property

    def set_private_property(self, value):
        if value > 0:  # Some validation
            self.__private_property = value

obj = MyClass(5)
print(obj.get_private_property())  # Output: 5

obj.set_private_property(10)
print(obj.get_private_property())  # Output: 10

# Direct access will raise an error
# print(obj.__private_property)  # AttributeError

# Accessing with name mangling (not recommended)
print(obj._MyClass__private_property)  # Output: 10
```

This approach ensures that the internal state of the object is protected and can only be accessed or modified through the provided methods, adhering to good object-oriented design principles.

## Properties

In Python, the `property()` function is a built-in function that creates and returns a property object. A property in Python provides a way to encapsulate instance variables (attributes) and control their access through getter, setter, and deleter methods. This allows you to define how an attribute is accessed and modified, enforcing validation or triggering specific actions when getting or setting the attribute.

### 1. **Basic Syntax of `property()`**

The `property()` function can be used in the following way:

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

- **`fget`:** Function to get the value of the property.
- **`fset`:** Function to set the value of the property.
- **`fdel`:** Function to delete the property.
- **`doc`:** String that contains the documentation for the property.

### 2. **Example: Using `property()` for a Getter and Setter**

Let’s go back to the `Person` class example and define the `age` property using the `property()` function:

```python
class Person:
    def __init__(self, age):
        self.__age = age  # This is the internal (private) attribute

    def get_age(self):
        """Getter method for age."""
        return self._age

    def set_age(self, value):
        """Setter method for age with validation."""
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer.")

    # Creating a property with the ideal name in this case 'age'
    age = property(get_age, set_age)

# Usage
try:
    person = Person(30)
    print(person.age)    # Calls get_age() method

    person.age = 25       # Calls set_age() method
    print(person.age)    # Calls get_age() method again

    person.age = -5       # Calls set_age(), triggers validation
except ValueError as e:
    print(e)             # Output: Age must be a non-negative integer.
```

### 3. **How It Works:**

- **`get_age`:** This method is called when you access the `age` property, like `person.age`.
- **`set_age`:** This method is called when you assign a value to `age`, like `person.age = 25`.
- **`age = property(get_age, set_age)`:** This line creates a property object `age` that uses `get_age` as the getter method and `set_age` as the setter method.

### 4. **Property with Deleter and Docstring**

You can also define a deleter method and provide a docstring for the property:

```python
class Person:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer.")

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age, "Property to get, set, or delete age.")

# Usage
person = Person(30)
print(person.age)           # Calls get_age()
person.age = 25             # Calls set_age()
del person.age              # Calls del_age()
print(Person.age.__doc__)   # Outputs the docstring: "Property to get, set, or delete age."
```

### 5. **Why Use `property()`?**

- **Encapsulation:** Properties allow you to hide internal implementation details of class attributes while still exposing them as accessible attributes. This helps in maintaining encapsulation.
- **Validation:** Using setters, you can enforce validation rules before allowing an attribute to be set.
- **Flexibility:** You can change the internal implementation without changing the external interface. For instance, you can change how an attribute is stored without affecting how it's accessed or modified by users of the class.
- **Compatibility:** Properties allow you to convert attributes to properties without changing the class interface. This is particularly useful for maintaining backward compatibility when refactoring code.

### 6. **Modern Alternative: Using Decorators**

While `property()` is a powerful feature, Python provides a more readable and modern approach using decorators (`@property`, `@<property_name>.setter`, and `@<property_name>.deleter`). This approach is more commonly used in modern Python code.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer.")

    @age.deleter
    def age(self):
        del self._age

# Usage
person = Person(30)
print(person.age)  # Calls age getter
person.age = 25    # Calls age setter
del person.age     # Calls age deleter
```

### Summary

The `property()` function is a powerful tool in Python classes for controlling access to attributes. It allows you to define getters, setters, and deleters, giving you fine-grained control over how attributes are managed. While decorators provide a more modern syntax for the same functionality, understanding `property()` is fundamental to grasping how Python properties work under the hood.

we can also just use one part of **property** doing so will result in a readonly attribute

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age


# Usage
person = Person(30)
print(person.age)  # Calls age getter
person.age = 25    # Calls age setter, this will raise an AttributeError: can't set attribute
```

### "\_" vs "\_\_"

In Python, the use of a single underscore `_` and double underscores `__` serves different purposes, particularly when naming class attributes:

### 1. **Single Underscore (`_`)**: _Protected_ Convention

- **Usage:** A single underscore before an attribute (e.g., `_age`) is a _convention_ used to indicate that the attribute is intended to be protected, meaning it is a part of the internal implementation and should not be accessed directly from outside the class.
- **Behavior:** It does not enforce any restrictions by the Python interpreter. It’s merely a signal to other developers that this attribute is intended for internal use only, and should be accessed via a method or property rather than directly.

```python
class Person:
    def __init__(self, age):
        self._age = age  # This is a protected attribute by convention

    def get_age(self):
        return self._age

person = Person(25)
print(person._age)  # Technically accessible, but not recommended
```

In this example, `_age` is a protected attribute by convention. It’s accessible from outside the class, but the single underscore signals that it’s not meant to be accessed directly.

### 2. **Double Underscore (`__`)**: _Private_ Convention with Name Mangling

- **Usage:** A double underscore before an attribute name (e.g., `__age`) triggers name mangling. This changes the name of the attribute internally to include the class name, making it harder to accidentally access or modify it from outside the class.
- **Behavior:** Python will change the name of the attribute to `_ClassName__attributeName`, making it less accessible from outside the class, effectively providing a stronger form of encapsulation.

```python
class Person:
    def __init__(self, age):
        self.__age = age  # This is a private attribute with name mangling

    def get_age(self):
        return self.__age

person = Person(25)
# print(person.__age)  # This would raise an AttributeError
print(person._Person__age)  # Accessing via name mangling (not recommended)
```

In this case, `__age` is intended to be private, and direct access like `person.__age` would fail. However, it’s still possible to access it using the mangled name, `person._Person__age`, though this is generally discouraged.

### **Why Use a Single Underscore (`_`) Instead of Double (`__`)**?

- **Single Underscore (`_`)**:

  - **Purpose:** The single underscore is a convention to indicate that the attribute is intended for internal use, but it’s still accessible from outside the class. This is useful when you want to signal to other developers that they should not touch this attribute directly, but you don't want to completely hide it.
  - **Simplicity:** It’s easier and cleaner when you don't need strict encapsulation, and you expect that developers using your class will respect the convention.

- **Double Underscore (`__`)**:
  - **Purpose:** The double underscore is used when you need to strongly indicate that the attribute should not be accessed or modified from outside the class. It enforces a stronger form of encapsulation through name mangling.
  - **Use Case:** It’s useful in situations where you’re developing a class library and want to prevent accidental access or modification of internal attributes.

### **Summary:**

- **Use `_` (single underscore) when you want to indicate that an attribute is for internal use only but do not need strict access control.**
- **Use `__` (double underscore) when you need to enforce stricter encapsulation and prevent the attribute from being easily accessed or modified from outside the class.**

In the example you referred to (`self._age = age`), a single underscore is used because it's a common practice in Python to denote protected attributes. If you require stricter encapsulation, you would use a double underscore instead.

## Inheritance
