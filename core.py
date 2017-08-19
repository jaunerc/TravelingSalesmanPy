import random
import math


class City:
    def __init__(self, name, pos, number):
        self.name = name
        self.pos = pos
        self.number = number


def random_cities(size, x_max, y_max):
    cities = []
    for i in range(0, size):
        cities.append(City(name=str(i), pos=random_vector(x_max, y_max), number=i))
    return cities


def random_vector(x_max, y_max):
    x = random.randint(0, x_max)
    y = random.randint(0, y_max)
    return (x, y)


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
    distance += calc_euclidean_distance(cities[len(cities) - 1].pos,
                                        cities[0].pos)  # The last path is to the first city
    return distance


def calc_euclidean_distance(v1, v2):
    return math.sqrt(math.pow(v1[0] - v2[0], 2) + math.pow(v1[1] - v2[1], 2))


# https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
def lexicographic_order(cities):
    largest_x = lexicographic_step_one(cities)
    if largest_x == -1:
        return
    largest_y = lexicographic_step_two(cities, largest_x)
    lexicographic_step_three(cities, largest_x, largest_y)
    lexicographic_step_four(cities, largest_x)


def lexicographic_step_one(cities):
    largest_x = -1
    for x in range(0, len(cities) - 1):
        if cities[x].number < cities[x + 1].number:
            largest_x = x
    return largest_x


def lexicographic_step_two(cities, largest_x):
    largest_y = -1
    for y in range(0, len(cities)):
        if cities[largest_x].number < cities[y].number:
            largest_y = y
    return largest_y


def lexicographic_step_three(cities, largest_x, largest_y):
    temp = cities[largest_x]
    cities[largest_x] = cities[largest_y]
    cities[largest_y] = temp


def lexicographic_step_four(cities, largest_x):
    sublist = cities[largest_x + 1: len(cities) - 1]
    del (cities[largest_x + 1: len(cities) - 1])
    sublist.reverse()
    cities += sublist


def calc_all_possible_paths(num_cities):
    return 0
