import pygame as py
import math

def get_points_after_rotation(x, y, angle):
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = y * math.cos(angle) + x * math.sin(angle)
    return x_new, y_new

def main():
    screen = py.display.set_mode((800, 600))
    screen.fill('white')
    x = 300
    y = 200
    angle = 0
    while angle < math.pi * 2:
        x, y = get_points_after_rotation(x-200, y-200, angle)
        x += 200
        y += 200
        py.draw.line(screen, 'BLUE', (200, 200), (x, y))
        angle += math.pi/16
    py.display.update()

main()
