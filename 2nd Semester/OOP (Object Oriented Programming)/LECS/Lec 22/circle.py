from shape import *

class Circle(Shape):
    def __init__(self, screen, center_x, center_y, radius, color='BLUE'):
        super().__init__(screen, color)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius

    def draw(self):
        py.draw.circle(self.screen, self.color, (self.__center_x, self.__center_y), self.__radius)
        py.display.update()
