from tkinter import *


def init_context():
    master = Tk()
    master.wm_title('TSP')
    return master


def create_canvas(master, width, height):
    return Canvas(master, width, height)
