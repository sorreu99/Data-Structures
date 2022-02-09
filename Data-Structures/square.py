from shape import Shape


class Square(Shape):
    def __init__(self, s1, s2, s3, s4):
        Shape.__init__(self, 4)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def get_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4

    def get_area(self):
        return self.s1 ** 2
