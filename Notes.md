# Python

## Intro

Python is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability and syntax that allows programmers to express concepts in fewer lines of code compared to other languages like C++ or Java.

### Key Features of Python:

1. **Simple and Easy to Learn**: Python's syntax is designed to be intuitive and its language constructs make it easy to learn, even for beginners.
2. **Versatile**: Python is a general-purpose language used for web development, data analysis, artificial intelligence, scientific computing, automation, and more.
3. **Interpreted Language**: Python code is executed line-by-line, which makes debugging easier but can impact performance.
4. **Extensive Standard Library**: Python comes with a large standard library that includes modules and packages for virtually every task, from file I/O to web development.
5. **Cross-Platform**: Python is available on multiple operating systems including Windows, macOS, and Linux, which allows for cross-platform development.
6. **Community Support**: Python has a large and active community, contributing to a wealth of third-party modules and tools, as well as extensive documentation and tutorials.

### Common Use Cases:

- **Web Development**: Frameworks like Django and Flask make Python a popular choice for backend web development.
- **Data Science and Machine Learning**: Libraries such as Pandas, NumPy, and Scikit-learn are widely used in data analysis and machine learning.
- **Automation**: Python's simplicity and readability make it an excellent choice for scripting and automating repetitive tasks.
- **Software Development**: Python is used in developing desktop applications, game development, and even network servers.

Python's combination of simplicity, versatility, and a strong support community has made it one of the most popular programming languages in the world.

## Python implementation and specification

Python has several implementations, each catering to different use cases and performance needs. Here’s an overview of the most notable implementations and the official specification that guides them:

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
     - Just-In-Time (JIT) compiler that translates Python code to machine code at runtime, offering significant speed improvements for many workloads.
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
     - Translates Python code into .NET Intermediate Language (IL), which can be executed by the Common Language Runtime (CLR).
     - Integrates with .NET libraries and services.
   - **Use Cases**: Applications that need to leverage .NET infrastructure or interact with other .NET languages.

5. **MicroPython**:
   - **Description**: A lean and efficient implementation of Python for microcontrollers and embedded systems.
   - **Features**:
     - Designed to run with limited resources.
     - Supports a subset of the Python standard library tailored for embedded development.
   - **Use Cases**: Embedded systems, Internet of Things (IoT) projects, and other resource-constrained environments.

### Python Language Specification

The Python language specification is outlined in the Python Enhancement Proposals (PEPs), which are documents that describe new features, processes, and information about the Python language. Key PEPs include:

1. **PEP 8**:

   - **Title**: Style Guide for Python Code
   - **Content**: Provides conventions for writing readable and maintainable Python code, including naming conventions, indentation, and more.

2. **PEP 20**:

   - **Title**: The Zen of Python
   - **Content**: A collection of aphorisms that capture the philosophy of Python, emphasizing simplicity, readability, and the importance of writing explicit code.

3. **PEP 484**:

   - **Title**: Type Hints
   - **Content**: Introduces optional type hinting to Python, enabling static type checking and better code clarity without changing the runtime behavior.

4. **PEP 257**:
   - **Title**: Docstring Conventions
   - **Content**: Guidelines for writing docstrings in Python, including conventions for formatting and content.

### Conclusion

The various implementations of Python cater to different needs, whether it's performance optimization with PyPy, integration with Java via Jython, or embedded systems development with MicroPython. The language specification, primarily driven by PEPs, ensures that Python maintains consistency, readability, and a coherent philosophy across its implementations.

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

Python is a **dynamic-typed language** which means variable types are determined at **run time** unlike **static-typed languages** which types are determined at **compile time**.

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

print(id(x))# => 1384214063408

x = x + 1


print(id(x))# => 1384214063440

nums = [1,2,4]
print(id(nums)) # => 2331135203072

nums.append(10)
print(id(nums)) # => 2331135203072

```
