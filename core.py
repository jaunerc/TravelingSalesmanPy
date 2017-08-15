import random

coordinates_x_max = 800
coordinates_y_max = 600


class City:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos


def random_cities(size):
    cities = []
    for i in range(0, size):
        cities.append(City(name=str(i), pos=random_vector()))
    return cities


def random_vector():
    x = random.randint(0, coordinates_x_max)
    y = random.randint(0, coordinates_y_max)
    return (x, y)
