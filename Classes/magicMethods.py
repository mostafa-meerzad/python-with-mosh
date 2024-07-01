class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})" # this string will be provided if an instance object of this class is being passed to "print" function

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other): 
        return self.x < other.x and self.y < other.y # by defining less-than operator python automatically figures out the greater-than operator as well
    
    def __add__ (self, other):
        return (self.x + other.x, self.y + other.y)

    def __len__(self):
        return 0
    
    def draw(self):
        print("drawing the point...")
        print(self.x)


myPoint = Point(1, 2)
print(myPoint.x)
myPoint.draw()

print(myPoint)
print(str(myPoint))

# ------------------

point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1  == point2) # => True
print(point1 < point2)
point2 = Point(1, 2)
print()
point1 = Point(1, 1)
point2 = Point(2, 2)
print(point1  == point2) # => False
print(point1 > point2)
print(point1 < point2)
print()

print(point1 + point2)
print(len(point1))
