from core import *


class SolveState:
    def __init__(self):
        self.best_path = math.pow(2, 32)
        self.finished = False


def solve_random_step(cities, state):
    is_best_path = False
    random.shuffle(cities)
    distance = calc_path_distance(cities)
    if state.best_path > distance:
        state.best_path = distance
        print("Current best: " + str(distance))
        is_best_path = True
    return is_best_path



