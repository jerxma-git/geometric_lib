import unittest

from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_normal_flow(self):
        res = area(2)
        self.assertAlmostEqual(res, 4)

    def test_area_floats(self):
        testcase_data = [
            (2.5, 6.25),
            (0.0, 0)
        ]
        for a, res in testcase_data:
            self.assertAlmostEqual(area(a), res)
    
    def test_perimeter_normal_flow(self):
        res = perimeter(2)
        self.assertAlmostEqual(res, 8)

    def test_perimeter_floats(self):
        testcase_data = [
            (2.5, 10),
            (0.0, 0)
        ]
        for a, res in testcase_data:
            self.assertAlmostEqual(perimeter(a), res)
    