from Figures.Circle import Circle
from Figures.Triangle import Triangle

if __name__ == '__main__':
    a = Triangle(3, 4, 5)
    print(a.calculate_square())
    print(a.is_exist())
    print(a.is_rectangular())

    b = Circle(3)
    print(b.calculate_square())
