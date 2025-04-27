import unittest

from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_normal_flow(self):
        res = area(2, 3)
        self.assertAlmostEqual(res, 6)

    def test_area_floats(self):
        testcase_data = [
            ((2, 3.5), 7),
            ((3.2, 3.2), 10.24),
            ((3.3, 1), 3.3)
        ]
        for (a,b), res in testcase_data:
            self.assertAlmostEqual(area(a, b), res)
    
    def test_perimeter_normal_flow(self):
        res = perimeter(2, 4)
        self.assertAlmostEqual(res, 12)

    def test_perimeter_floats(self):
        testcase_data = [
            ((2, 3.5), 11),
            ((3.2, 3.2), 12.8),
            ((3.3, 1), 8.6)
        ]
        for (a,b), res in testcase_data:
            self.assertAlmostEqual(perimeter(a, b), res)
    