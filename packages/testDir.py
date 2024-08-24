# print(dir()) # returns a list of valid attributes and methods


class SimpleClass:

    def __init__(self):
        self.x = 1

    def simple_method(self):
        return "Hello, world"
    

# creating an object
simple_obj = SimpleClass()

print(dir(simple_obj)) # a lis of valid attributes both defined/inherited ones
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'simple_method', 'x']

print(__name__)