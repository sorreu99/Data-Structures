import shape


class Triangle(shape.Shape):
    def __init__(self, a, b, c):
        shape.Shape.__init__(self, 3)
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s*(s - self.side1)*(s - self.side2)*(s - self.side3)) ** (1 / 2)
