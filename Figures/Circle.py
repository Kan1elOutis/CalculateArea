from Figures.Figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, r):
        if (not isinstance(r, int) and not isinstance(r, float)) or r < 0:
            raise Exception("Not valid arguments")
        self.r = r

    def calculate_square(self):
        return round(pi * (self.r ** 2), 2)
