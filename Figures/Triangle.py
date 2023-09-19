from Figures.Figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        for item in [a, b, c]:
            if (not isinstance(item, int) and not isinstance(item, float)) or item < 0:
                raise Exception("Not valid arguments")
        self.a = a
        self.b = b
        self.c = c

    def calculate_square(self):
        if self.is_exist() == True:
            semi_perimeter = (self.a + self.b + self.c) / 2
            square = (semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (
                    semi_perimeter - self.c)) ** 0.5

            return square
        else:
            return "123"

    def is_exist(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            raise Exception("some side is less than 0")
        else:
            if (self.a >= (self.b + self.c)
                    or self.b >= (self.a + self.c)
                    or self.c >= (self.a + self.b)):
                raise Exception("side smaller than the other two")

        return True

    def is_rectangular(self):
        a, b, c = sorted([self.a, self.b, self.c])
        return True if a ^ 2 + b ^ 2 == c ^ 2 else False
