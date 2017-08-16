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
