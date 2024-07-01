class Point:
    # every class method must take at least one parameter called "self"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("drawing the point")
        print(f"points x:{self.x}, y:{self.y}")


myPoint = Point(1, 5)

print(myPoint.x)
print(myPoint.y)
print(myPoint.draw())

print()
print(type(myPoint))
print(isinstance(myPoint, Point))
print(isinstance(myPoint, int))

point1 = Point(3, 5)
point2 = Point(6, 5)

print(point1.x)
print(point1.y)
print(point1.draw())
point1.z = 10
point1.x = 0
print(point1.x)
print(point1.z)
print()
print(point2.x)
print(point2.y)
print(point2.draw())


# ----------------------------------------
class Point:
    defaultColor = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("drawing the point")
        print(f"points x:{self.x}, y:{self.y}")


point1 = Point(3, 5)
point2 = Point(6, 5)

print(point1.x)
print(point1.y)
print(point1.draw())
point1.z = 10
point1.x = 0
print(point1.x)
print(point1.z)
print(f"default color in point1 object: {point1.defaultColor}")
print(f"default color in point2 object: {point2.defaultColor}")
print(f"default color in Point class: {Point.defaultColor}")

Point.defaultColor = "yellow"  # changing a class attribute will be seen in all instances objects of that class

print(f"default color in point1 object: {point1.defaultColor}")
print(f"default color in point2 object: {point2.defaultColor}")
print(f"default color in Point class: {Point.defaultColor}")
# ----------------------------------


class Point:
    defaultColor = "red"

    def __init__(self) -> None:
        pass

    @classmethod
    def classMethod(cls):
        print(cls.defaultColor)

        print("I'm a class method")


myPoint = Point()
myPoint.classMethod()