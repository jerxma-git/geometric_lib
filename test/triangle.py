import unittest

from triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_normal_flow(self):
        res = area(2, 3)
        self.assertAlmostEqual(res, 3)

    def test_area_floats(self):
        testcase_data = [
            ((2, 3.5), 3.5),
            ((3.2, 3.2), 5.12),
            ((3.3, 1), 1.65)
        ]
        for (a,b), res in testcase_data:
            self.assertAlmostEqual(area(a, b), res)
    
    def test_perimeter_normal_flow(self):
        res = perimeter(2, 4, 3)
        self.assertAlmostEqual(res, 9)

    def test_perimeter_floats(self):
        testcase_data = [
            ((2, 3.5, 2.4), 7.9),
            ((3.2, 3.2, 3.2), 9.6),
            ((3.3, 1, 3.7), 8)
        ]
        for (a, b, c), res in testcase_data:
            self.assertAlmostEqual(perimeter(a, b, c), res)
    