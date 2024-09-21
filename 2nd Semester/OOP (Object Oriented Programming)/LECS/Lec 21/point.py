class Point:
    def __init__(self, x, y):
        self.set(x, y)

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f'X: {self.__x} Y: {self.__y} '
