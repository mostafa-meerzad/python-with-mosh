# Docstring

Docstrings in Python are **special strings** used to document code. They provide a convenient way to describe what a
module, class, function, or method does. Docstrings are enclosed in triple quotes (`"""` or `'''`) and are typically the
first statement in the definition of a module, class, or function.

### Key Features of Docstrings

1. **Easy Documentation**: They serve as in-code documentation, making your code easier to understand and maintain.
2. **Accessible at Runtime**: You can access docstrings programmatically using the `.__doc__` attribute.
3. **Standard Format**: Following a standardized format, like [PEP 257](https://peps.python.org/pep-0257/), improves
   readability and tool compatibility.

---

### Syntax

**Single-line docstring**:

```python
def greet():
    """Greet the user."""
    print("Hello!")
```

**Multi-line docstring**:

```python
def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of the two numbers.
    """
    return a + b
```

---

### Where Docstrings Are Used

1. **Modules**: Document the purpose of the module.
   ```python
   """This module provides utilities for mathematical operations."""
   ```

2. **Classes**: Describe the class and its purpose.
   ```python
   class Animal:
       """A class representing an animal."""
       def __init__(self, name):
           self.name = name
   ```

3. **Functions/Methods**: Explain the function's behavior, inputs, and outputs.
   ```python
   def multiply(a, b):
       """Multiply two numbers."""
       return a * b
   ```

---

### Accessing Docstrings

You can access a docstring using the `.__doc__` attribute:

```python
def greet():
    """Greet the user."""
    print("Hello!")


print(greet.__doc__)  # Output: Greet the user.
```

---

### Best Practices

1. **Be Concise but Informative**: Explain **what** the code does, not **how** it does it.
2. **Follow PEP 257**: Use consistent formatting to ensure compatibility with tools like Sphinx or IDE documentation
   generators.
3. **Include Arguments and Return Values**: For functions/methods, describe the inputs, outputs, and exceptions (if
   any).

Example:

```python
def divide(a, b):
    """
    Divide two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
```

By consistently using docstrings, you create more maintainable and user-friendly code!

## Example

The standard structure for **docstrings**:

The first line should be a short description followed by a blank line and then comes the full detailed explanation.

```python
"""
One line description.

A more detailed explanation  
"""
```

If you are dealing with a simple case using a single line Docstring is enough

```python
"""Greet the user."""

def greet(name):
    print(f"Hello {name}")
```