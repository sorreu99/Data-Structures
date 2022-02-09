import shape


class Rectangle(shape.Shape):
    def __init__(self, a, b, c, d):
        shape.Shape.__init__(self, 4)
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

    def get_area(self):
        l = self.side1
        if self.side1 == self.side2:
            w = self.side3
        else:
            w = self.side2
        return l * w
