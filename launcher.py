from ui import *
from solver import *
from core import *
import time

coordinates_x_max = 800
coordinates_y_max = 600
num_cities = 8
num_possible_paths = int(calc_all_symmetric_paths(num_cities))

cities = random_cities(num_cities, coordinates_x_max, coordinates_y_max)

user_interface = GraphicalInterface(coordinates_x_max, coordinates_y_max, num_possible_paths)
solve_state = SolveState()


def solve():
    # return solve_random_step(cities, solve_state)
    return solve_lexicographic_symmetric_step(cities, solve_state)


def draw(is_best_path, progress):
    user_interface.draw(cities, is_best_path, progress)


for progress in range(0, num_possible_paths):
    is_best_path = solve()
    draw(is_best_path, progress + 1)

# main loop
# while not solve_state.finished:
#   is_best_path = solve()
#  draw(is_best_path)
# time.sleep(1)

draw_end_state(user_interface.canvas, cities)
print("All paths checked.")
user_interface.freeze()
