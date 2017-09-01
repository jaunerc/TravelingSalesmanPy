import unittest
from core import *

x_max = 800
y_max = 600


class CoreTest(unittest.TestCase):
    def test_random_vector_xgte_zero(self):
        vector = random_vector(x_max, y_max)
        self.assertGreaterEqual(vector[0], 0)

    def test_random_vector_ygte_zero(self):
        vector = random_vector(x_max, y_max)
        self.assertGreaterEqual(vector[1], 0)

    def test_random_vector_xlte_max(self):
        vector = random_vector(x_max, y_max)
        self.assertLessEqual(vector[0], x_max)

    def test_random_vector_ylte_max(self):
        vector = random_vector(x_max, y_max)
        self.assertLessEqual(vector[1], y_max)

    def test_lexicographic_step_one(self):
        cities = random_cities(10, 100, 100)
        self.assertEqual(lexicographic_step_one(cities), 8)

    def test_lexicographic_step_two(self):
        cities = random_cities(10, 100, 100)
        self.assertEqual(lexicographic_step_two(cities, 8), 9)

    def test_lexicographic_step_three(self):
        cities = random_cities(10, 100, 100)
        lexicographic_step_three(cities, 8, 9)
        self.assertEqual(cities[9].number, 8)

    def test_lexicographic_step_four(self):
        cities = random_cities(10, 100, 100)
        largest_x = 8
        lexicographic_step_three(cities, largest_x, 9)
        lexicographic_step_four(cities, largest_x)
        self.assertEqual(cities[9].number, 8)

    def test_calc_all_possible_paths(self):
        self.assertEqual(calc_all_symmetric_paths(5), 12)

    def test_calc_all_possible_paths_low(self):
        self.assertEqual(calc_all_symmetric_paths(2), 1)

    def test_calc_all_asymmetric_paths(self):
        self.assertEqual(calc_all_asymmetric_paths(3), 2)
