import math

class Point:
    count = 0
    def __init__(self):
        self.x = 0
        self.y = 0
        Point.count += 1

    def __del__(self):
        Point.count -= 1
    
    def get_count():
        return Point.count
    
    def set(self, x, y):
        self.x = x
        self.y = y

    # <------------ Question 1 (a) ------------> #
    def reverse(self):
        self.x = -(self.x)
        self.y = -(self.y)


    # <------------ Question 1 (b) ------------> #
    def quadrant(self):
        if self.x >= 0 and self.y >= 0:
            return('These points exist in the 1st Quadrant')
        elif self.x < 0 and self.y > 0:
            return('These points exist in the 2nd Quadrant')
        elif self.x < 0 and self.y < 0:
            return('These points exist in the 3rd Quadrant')
        elif self.x > 0 and self.y < 0:
            return('These points exist in the 4th Quadrant')


    # <------------ Question 1 (c) ------------> #

    def rotate_points(self, theta):
        new_obj = Point()
        new_obj.x = int(((self.x)*(math.cos(theta))) + ((self.y)*(math.sin(theta))))
        new_obj.y = int(((-(self.x))*(math.sin(theta))) + ((self.y)*(math.cos(theta))))
        return new_obj

    def show(self):
        print(f'({self.x}, {self.y})')

    # <------------ Question 1 (d) ------------> #
    def __str__(self):
        return(f'({self.x}, {self.y})')


    # <------------ Question 1 (e) ------------> #
    def compare_rotation(self,theta):
        x_float = ((self.x)*(math.cos(theta))) + ((self.y)*(math.sin(theta)))
        y_float = (-(self.x)*(math.sin(theta))) + ((self.y)*(math.cos(theta)))
        x_int = int(((self.x)*(math.cos(theta))) + ((self.y)*(math.sin(theta))))
        y_int = int((-(self.x)*(math.sin(theta))) + ((self.y)*(math.cos(theta))))
        d = (((x_float - x_int)**2) + ((y_float - y_int) **2))**0.5
        return d
def main():
    p1 = Point()
    p2 = Point()
    p1.set(0,5)
    p1.show()
    print(Point.get_count())

    #             # <------------ Question 1 (a) ------------> #
    # # p1.reverse()

    #             # <------------ Question 1 (b) ------------> #
    # print(p1.quadrant())

    #             # <------------ Question 1 (c) ------------> #
    # for i in range(12):

    #     new = p1.rotate_points(60)
    # new.show()

    #             # <------------ Question 1 (d) ------------> #
    # # print(p1)
    #             # <------------ Question 1 (e) ------------> #
    # print(p1.compare_rotation(60))
main()
