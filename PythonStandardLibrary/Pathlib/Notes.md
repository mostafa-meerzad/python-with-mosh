# Python Standard Library

## Pathlib module

The `pathlib` module in Python provides an object-oriented approach to working with file system paths. It was introduced in Python 3.4 as a more intuitive and versatile alternative to the older `os.path` module. The `pathlib` module makes it easier to work with paths by treating them as objects rather than strings, allowing for more readable and manageable code.

### Key Concepts of the `pathlib` Module

1. **Path Objects**:

   - `pathlib.Path`: The main class used to represent a file or directory path. It can represent both relative and absolute paths.
   - `PosixPath` and `WindowsPath`: These are subclasses of `Path` used internally to handle platform-specific path conventions.

   ```python
   from pathlib import Path

   # Creating a Path object
   path = Path('some_directory/some_file.txt')
   ```

2. **Basic Operations**:

   - **Joining Paths**: You can use the `/` operator to join paths, making it more intuitive than using `os.path.join()`.
     ```python
     path = Path('some_directory') / 'some_subdirectory' / 'some_file.txt'
     ```
   - **Checking Existence**: Use `exists()` to check if a path exists.
     ```python
     if path.exists():
         print("Path exists")
     ```
   - **File/Directory Attributes**: You can check various attributes like whether a path is a file, directory, etc.
     ```python
     if path.is_file():
         print("This is a file")
     if path.is_dir():
         print("This is a directory")
     ```

3. **Reading and Writing Files**:

   - **Reading**: You can open and read a file using the `read_text()` method.
     ```python
     content = path.read_text()
     ```
   - **Writing**: Similarly, you can write to a file.
     ```python
     path.write_text("Some text")
     ```

4. **Directory Operations**:

   - **Listing Directory Contents**: Use `iterdir()` to iterate over the contents of a directory.
     ```python
     directory = Path('some_directory')
     for file in directory.iterdir():
         print(file)
     ```
   - **Creating Directories**: Use `mkdir()` to create a directory.
     ```python
     path.mkdir(parents=True, exist_ok=True)
     ```

5. **Path Properties**:

   - **Name, Stem, and Suffix**:
     - `name`: Full name of the file or directory (e.g., `'some_file.txt'`).
     - `stem`: The name without the file extension (e.g., `'some_file'`).
     - `suffix`: The file extension (e.g., `'.txt'`).
     ```python
     print(path.name)    # some_file.txt
     print(path.stem)    # some_file
     print(path.suffix)  # .txt
     ```

6. **Relative and Absolute Paths**:
   - **Absolute Path**: Use `resolve()` or `absolute()` to get the absolute path.
     ```python
     absolute_path = path.resolve()
     ```
   - **Relative Path**: Use `relative_to()` to find the relative path to another path.
     ```python
     relative_path = path.relative_to('some_directory')
     ```

### Example Usage

```python
from pathlib import Path

# Create a Path object for a file
file_path = Path('example_directory/example_file.txt')

# Check if the file exists
if file_path.exists():
    # Read the content of the file
    content = file_path.read_text()
    print(content)

# Create a new directory
new_dir = Path('new_directory')
new_dir.mkdir(parents=True, exist_ok=True)

# Create a new file and write to it
new_file = new_dir / 'new_file.txt'
new_file.write_text("Hello, World!")

# List contents of a directory
for item in new_dir.iterdir():
    print(item)
```

### Benefits of Using `pathlib`

- **Readability**: The object-oriented approach is more readable and intuitive.
- **Cross-Platform**: `pathlib` handles differences between Windows and POSIX systems, making the code more portable.
- **Versatility**: It can handle various file system operations in a unified way, reducing the need for multiple modules (`os`, `shutil`, etc.).

Overall, `pathlib` is a powerful and modern way to handle file system paths in Python, making code easier to write, understand, and maintain.
