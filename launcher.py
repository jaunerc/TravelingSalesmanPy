from ui import *
from solver import *
from core import *
import time

coordinates_x_max = 800
coordinates_y_max = 600
num_cities = 8

cities = random_cities(num_cities, coordinates_x_max, coordinates_y_max)

user_interface = GraphicalInterface(coordinates_x_max, coordinates_y_max)
solve_state = SolveState()


def solve():
    return solve_random_step(cities, solve_state)


def draw(is_best_path):
    user_interface.draw(cities, is_best_path)


# main loop
while True:
    is_best_path = solve()
    draw(is_best_path)
    # time.sleep(3)

# user_interface.freeze()
