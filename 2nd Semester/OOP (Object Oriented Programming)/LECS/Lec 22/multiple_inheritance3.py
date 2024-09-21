class P1:
    def __init__(self, a):
        self.__a = a
    def __str__(self):
        return f'A: {self.__a} '

class P2:
    def __init__(self, b):
        self.__b = b
    def __str__(self):
        return f'B: {self.__b} '

#I have changed the order of inheritance, now code will give error
class C(P2, P1):
    def __init__(self, a, b, c):
        super().__init__(a)
        P2.__init__(self, b)
        self.__c = c

    def __str__(self):
        return f'{P1.__str__()}{P2.__str__(self)}C: {self.__c} '

def main():
    object_c = C(1,2,3)
    print(object_c)

main()
