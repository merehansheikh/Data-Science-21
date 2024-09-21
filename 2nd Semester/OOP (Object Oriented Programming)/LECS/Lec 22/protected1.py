class P:
    def __init__(self, p):
        self._p = p
    def __str__(self):
        return f'P: {self._p} '

class C(P):
    def __init__(self, p, c):
        super().__init__(p)
        self.__c = c

    def __str__(self):
        return f'{super().__str__()}C: {self.__c} '

    def set(self, p, c):
        self._p = p
        self.__c = c

def main():
    object_c = C(1,2)
    print(object_c)
    object_c.set(4,5)
    print(object_c)
    print(object_c._p)
    object_p = P(10)
    print(object_p)
    print(object_p._p)

main()
