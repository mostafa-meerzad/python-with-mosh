# Classes

In Python, classes are a fundamental part of object-oriented programming (OOP). A class defines a blueprint for creating objects (instances), allowing you to bundle data (attributes) and behaviors (methods) together.

### Basic Structure of a Class

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
