from tkinter import *

city_radius = 5
lines = []


class GraphicalInterface:
    def __init__(self, width, height):
        self.master = create_context()
        self.canvas = create_canvas(self.master, width, height)

    def draw(self, cities):
        clear_current_path(self.canvas)
        draw_cities(self.canvas, cities)
        draw_current_path(self.canvas, cities)
        self.master.update_idletasks()
        self.master.update()

    def freeze(self):
        self.master.mainloop()


def create_context():
    master = Tk()
    master.wm_title('TSP')
    return master


def create_canvas(master, width, height):
    canvas = Canvas(master, width=width, height=height)
    canvas.configure(background="black")
    canvas.pack()
    return canvas


def clear_current_path(canvas):
    for line in lines:
        canvas.delete(line)


def draw_cities(canvas, cities):
    for city in cities:
        start = (city.pos[0] - city_radius, city.pos[1] - city_radius)
        end = (city.pos[0] + city_radius, city.pos[1] + city_radius)
        canvas.create_oval(start[0], start[1], end[0], end[1], fill="white")


def draw_current_path(canvas, cities):
    for i in range(0, len(cities) - 1):
        start = cities[i].pos
        end = cities[i + 1].pos
        lines.append(canvas.create_line(start[0], start[1], end[0], end[1], fill="white"))
