import unittest
from Figures.Circle import Circle
from Figures.Triangle import Triangle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circleA = Circle(3)
        self.circleB = Circle(4)

    def test_calc(self):
        self.assertEqual(self.circleA.calculate_square(), 28.27)
        self.assertEqual(self.circleB.calculate_square(), 50.27)


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangleA = Triangle(3, 4, 5)
        self.triangleB = Triangle(1, 2, 3)

    def test_calc(self):
        self.assertEqual(self.triangleA.calculate_square(), 6)
        with self.assertRaises(Exception):
            self.triangleB.calculate_square()

    def test_isExist(self):
        self.assertEqual(self.triangleA.is_exist(), True)
        with self.assertRaises(Exception):
            self.triangleB.is_exist()

    def test_isRectangular(self):
        self.assertEqual(self.triangleA.is_rectangular(), True)
        self.assertEqual(self.triangleB.is_rectangular(), False)
