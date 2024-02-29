import unittest

from circle import area, perimeter
from math import pi

class CircleTestCase(unittest.TestCase):
    def test_area_normal_flow(self):
        res = area(2)
        self.assertAlmostEqual(res, 4 * pi)

    def test_area_floats(self):
        testcase_data = [
            (2.5, 6.25 * pi),
            (0, 0)
        ]
        for r, res in testcase_data:
            self.assertAlmostEqual(area(r), res)
    
    def test_perimeter_normal_flow(self):
        res = perimeter(2)
        self.assertAlmostEqual(res, 4 * pi)

    def test_perimeter_floats(self):
        testcase_data = [
            (2.5, 5 * pi),
            (0, 0)
        ]
        for r, res in testcase_data:
            self.assertAlmostEqual(perimeter(r), res)
    