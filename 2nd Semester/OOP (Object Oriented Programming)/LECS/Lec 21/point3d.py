from point import *

class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.__z = z

    def __str__(self):
        return Point.__str__(self) + f'Z: {self.__z}'

