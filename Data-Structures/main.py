import rectangle
from square import Square
from triangle import Triangle

triangle1 = Triangle(12, 10, 5)
rectangle2 = rectangle.Rectangle(4, 5, 4, 5)
square1 = Square(4, 4, 4, 4)
print(triangle1.get_perimeter())
print(triangle1.get_area())
print(rectangle2.get_perimeter())
print(rectangle2.get_area())
print(square1.get_area())
print(square1.get_perimeter())