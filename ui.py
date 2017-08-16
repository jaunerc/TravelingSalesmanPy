from tkinter import *


class GraphicalInterface:
    def __init__(self, width, height):
        self.master = create_context()
        self.canvas = create_canvas(self.master, width, height)

    def draw(self, cities):
        draw_cities(self.canvas, cities)
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


def draw_cities(canvas, cities):
    for city in cities:
        canvas.create_oval(city.pos[0], city.pos[1], city.pos[0] + 10, city.pos[1] + 10, fill="white")
