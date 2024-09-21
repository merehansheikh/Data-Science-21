from shape import *

class Line(Shape):
    def __init__(self, screen, x1, y1, x2, y2, color='BLUE'):
        super().__init__(screen, color)
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def draw(self):
        py.draw.line(self.screen, self.color, (self.__x1, self.__y1), (self.__x2, self.__y2))
        py.display.update()
