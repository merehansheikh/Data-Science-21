import pygame as py
from circle import *
from line import *
from sun import *

def main():
    screen = py.display.set_mode((800, 600))
    screen.fill('white')
    py.display.update()
    line = Line(screen, 100, 100, 200, 200)
    circle = Circle(screen, 450, 250, 50)
    line.draw()
    circle.draw()
    #sun = Sun(screen, 450, 100, 50)
    #sun.draw()

main()
