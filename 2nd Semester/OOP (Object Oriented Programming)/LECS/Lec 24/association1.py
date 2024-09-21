class A(object):
    def __init__(self, n, x1, x2):
        self.n = n
        self.x1 = x1
        self.x2 = x2

class B(object):
    def __init__(self, y1, y2):
        self.y1 = y1
        self.y2 = y2

    def addAllNums(self, num1, num2):
        return self.y1 + self.y2 + num1 + num2

objA = A(1, 2, 6)
objB = B(5, 9)

sum = objB.addAllNums(objA.n, objA.x2)
print (f'Sum of all values: {sum}')
