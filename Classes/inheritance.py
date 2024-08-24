class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__() # by adding this line the constructor of super-class "Animal" will execute
        # it is not mandatory to call "super()" in the first line we can change the order in any way that suits
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.walk()
m.eat()
print(m.age)  # OK, before adding a constructor to the Mammal class
print(m.age)  # now raises: AttributeError: 'Mammal' object has no attribute 'age'
# which is caused by not calling the super-class's constructor
print()

f = Fish()
f.eat()
f.swim()
print(f.age)

print()
print(isinstance(f, Animal))  # True
print(isinstance(f, Fish))  # True
print(isinstance(f, Mammal))  # False

print(issubclass(Fish, Animal))  # True

# ------------------------------------------------------
# now if we define a constructor in Mammal and Fish classes the constructor of Animal will be overridden and only the constructors defined in sub-classes will execute
