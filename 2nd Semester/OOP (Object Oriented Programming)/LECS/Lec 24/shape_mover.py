from circle import *

class Shape_Mover():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_points_after_rotation(x, y, angle):
        x_new = x * math.cos(angle) - y * math.sin(angle)
        y_new = y * math.cos(angle) + x * math.sin(angle)
        return x_new, y_new

    def move(self, circle):
        rx = self.width // 2
        ry = self.height // 2
        fac = math.pi / 32
        angle = math.pi
        angle_end = 0
        x, y = circle.get_center()
        while angle >= angle_end :
            x_n, y_n = Shape_Mover.get_points_after_rotation(x - rx , y - ry, angle)
            x_n += rx
            y_n += ry
            circle.move(x_n, y_n)
            angle -= fac
