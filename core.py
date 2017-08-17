import random


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
