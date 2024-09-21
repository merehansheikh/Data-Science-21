from shape import *
import pygame as py
import time

class Sun(Shape):
    def __init__(self, screen, center_x, center_y, radius, color=(255,170,0)):
        super().__init__(screen, color)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius
        self.__distance = radius // 5

    def get_points_after_rotation(x, y, angle):
        x_new = x * math.cos(angle) - y * math.sin(angle)
        y_new = y * math.cos(angle) + x * math.sin(angle)
        return x_new, y_new

    def draw(self):
        py.draw.circle(self.screen, self.color, (self.__center_x, self.__center_y), self.__radius)
        x1 = self.__center_x + self.__radius + self.__distance
        x2 = self.__center_x + self.__radius + self.__distance + self.__distance
        y1 = self.__center_y
        y2 = self.__center_y
        pi_2 = math.pi * 2
        inc = math.pi / 16
        angle = 0
        while angle < pi_2 :
            x1, y1 = Sun.get_points_after_rotation(x1 - self.__center_x , y1 - self.__center_y, angle)
            x1 += self.__center_x
            y1 += self.__center_y
            x2, y2 = Sun.get_points_after_rotation(x2 - self.__center_x , y2 - self.__center_y, angle)
            x2 += self.__center_x
            y2 += self.__center_y
            py.draw.line(self.screen, self.color, (x1, y1), (x2, y2))
            angle += inc
        py.display.update()

    def erase(self):
        py.draw.circle(self.screen, 'WHITE', (self.__center_x, self.__center_y), self.__radius)
        x1 = self.__center_x + self.__radius + self.__distance
        x2 = self.__center_x + self.__radius + self.__distance + self.__distance
        y1 = self.__center_y
        y2 = self.__center_y
        pi_2 = math.pi * 2
        inc = math.pi / 16
        angle = 0
        while angle < pi_2 :
            x1, y1 = Sun.get_points_after_rotation(x1 - self.__center_x , y1 - self.__center_y, angle)
            x1 += self.__center_x
            y1 += self.__center_y
            x2, y2 = Sun.get_points_after_rotation(x2 - self.__center_x , y2 - self.__center_y, angle)
            x2 += self.__center_x
            y2 += self.__center_y
            py.draw.line(self.screen, 'WHITE', (x1, y1), (x2, y2))
            angle += inc
        py.display.update()

    def get_center(self): return self.__center_x, self.__center_y
    def set_center(self,x, y):
        self.__center_x = x
        self.__center_y = y

    def move(self,x, y):
        #self.erase()
        self.__center_x = x
        self.__center_y = y
        #if x > 0 and x < w and y > 0 and y < h:
        #time.sleep(0.1)
        self.draw()

