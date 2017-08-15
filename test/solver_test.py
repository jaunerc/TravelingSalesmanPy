import unittest

import core
from solver import *


class SolverTest(unittest.TestCase):
    def test_calc_path_distance(self):
        cities = [core.City("", (0, 0)), core.City("", (5, 5))]
        self.assertAlmostEqual(calc_path_distance(cities), math.sqrt(50), delta=0.1)

    def test_calc_euclidean_distance(self):
        v1 = (0, 0)
        v2 = (8, 8)
        self.assertAlmostEqual(calc_euclidean_distance(v1, v2), math.sqrt(128), delta=0.1)
