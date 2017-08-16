from ui import *
from solver import *
from core import *

coordinates_x_max = 800
coordinates_y_max = 600
num_cities = 10

cities = random_cities(num_cities, coordinates_x_max, coordinates_y_max)

user_interface = GraphicalInterface(coordinates_x_max, coordinates_y_max)
solve_state = SolveState()


def solve():
    solve_random_step(cities, solve_state)


def draw():
    user_interface.draw(cities)


# main loop
for i in range(0, 10):
    solve()
    draw()

user_interface.freeze()
