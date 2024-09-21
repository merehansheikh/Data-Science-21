from pickle import *

class Point2D:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def __str__(self):
        return f'X: {self.__x}, Y: {self.__y}'

class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
    def __str__(self):
        return super().__str__() + f'\tZ: {self.__z}'

points = []
points.append(Point2D(1, 2))
points.append(Point3D(4, 5, 6))
points.append(Point2D(7, 8))
points.append(Point2D(6, 3))
points.append(Point3D(3, 5, 1))

file = open('points.bin', mode='wb')

for point in points:
    dump(point, file)
file.close()

print ('---------------')
file = open('points.bin', mode='rb')
# p2 = loads(file)
# print(p2)
try:
    while True:
        point = load(file)
        print(point)
except:
    pass