# polymorphism.py

class Rectangle:

    def area(self):
        length = 8
        breadth = 5
        print("Rectangle Area:", length * breadth)


class Circle:

    def area(self):
        radius = 7
        print("Circle Area:", 3.14 * radius * radius)


class Square:

    def area(self):
        side = 6
        print("Square Area:", side * side)


shapes = [Rectangle(), Circle(), Square()]

for shape in shapes:
    shape.area()