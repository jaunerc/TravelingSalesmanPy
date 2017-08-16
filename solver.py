import random
import math


class SolveState:
    def __init__(self):
        self.best_path = 0
        self.finished = False


def solve_random_step(cities, state):
    random.shuffle(cities)
    distance = calc_path_distance(cities)
    if state.best_path > distance:
        state.best_path = distance

    print_current_path(cities)
    print(str(distance))


def print_current_path(cities):
    path = "Current path "
    for city in cities:
        path += city.name + ", "
    print(path)


def calc_path_distance(cities):
    distance = 0
    for i in range(0, len(cities) - 1):
        v1 = cities[i].pos
        v2 = cities[i + 1].pos
        distance += calc_euclidean_distance(v1, v2)

    return distance


def calc_euclidean_distance(v1, v2):
    return math.sqrt(math.pow(v1[0] - v2[0], 2) + math.pow(v1[1] - v2[1], 2))
