# import pdf2text
from pdf2text import convert


def greet(name):
    """Greet the user."""
    print(f"Hello {name}")


greet("Mostafa")


convert("test/path")