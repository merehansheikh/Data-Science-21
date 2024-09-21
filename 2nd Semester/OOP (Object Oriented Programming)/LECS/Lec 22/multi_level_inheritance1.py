class GP:
    def __init__(self, gp):
        self.__gp = gp
    def __str__(self):
        return f'GP: {self.__gp} '

class P(GP):
    def __init__(self, gp, p):
        GP.__init__(self, gp)
        self.__p = p
    def __str__(self):
        return f'{GP.__str__(self)} P: {self.__p} '

class C(P):
    def __init__(self, gp, p, c):
        P.__init__(self, gp, p)
        self.__c = c

    def __str__(self):
        return f'{P.__str__(self)}C: {self.__c} '

def main():
    object_c = C(1,2,3)
    print(object_c)
    print(object_c.__class__)
main()
