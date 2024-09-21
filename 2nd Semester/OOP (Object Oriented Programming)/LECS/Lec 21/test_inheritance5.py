class P:
    def __init__(self):
        print('Init function from parent is called')
        self.__x = 0

    def get_x(self):
        return self.__x

class C(P):
    def __init__(self):
        print('Init function from child is called')
        P.__init__(self)

def main():
    object = C()
    print (object.get_x())

main()

