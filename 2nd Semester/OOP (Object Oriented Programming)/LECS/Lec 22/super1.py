class P:
    def __init__(self, p):
        self.__p = p
    def __str__(self):
        return f'P: {self.__p} '

class C(P):
    def __init__(self, p, c):
        super().__init__(p)
        self.__c = c

    def __str__(self):
        return f'{super().__str__()}C: {self.__c} '

def main():
    object_c = C(1,2)
    print(object_c)

main()
