from shape import *
from time import *

class Circle(Shape):
    def __init__(self, screen, center_x, center_y, radius, color='BLUE'):
        super().__init__(screen, color)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius

    def get_center(self):
        return self.__center_x, self.__center_y
    def set_center(self, x, y):
        self.__center_x = x
        self.__center_y = y
    def draw(self):
        py.draw.circle(self.screen, self.color, (self.__center_x, self.__center_y), self.__radius)
        py.display.update()
    def move(self, x, y):
        py.draw.circle(self.screen, 'WHITE', (self.__center_x, self.__center_y), self.__radius)
        sleep(0.5)
        self.set_center(x, y)
        py.draw.circle(self.screen, self.color, (self.__center_x, self.__center_y), self.__radius)
        py.display.update()
