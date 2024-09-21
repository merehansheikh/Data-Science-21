import pygame as py
from circle import *
from shape_mover import *

def main():
    screen = py.display.set_mode((1200, 800))
    screen.fill('white')
    py.display.update()
    circle = Circle(screen, 500, 300, 40)
    sm = Shape_Mover(1200, 800)
    sm.move(circle)

main()

