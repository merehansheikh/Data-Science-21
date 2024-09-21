class P:
    def pf():
        print ('Paaaaaaaaarent')

class C(P):
    def cf():
        print ('Childddddddddd')

class Dummy:
    def dummy():
        print ('I am dummy like PM')

def main():
    object_c = C()
    object_p = P()
    print (f'Is object_c is of class C? {issubclass(C, P)}')
    print (f'Is object_c is of class P? {issubclass(C, P)}')
    print (f'Is object_c is of class Dummy? {issubclass(C, P)}')
    print (f'Is P is of class C? {issubclass(P, C)}')
    print (f'Is P is of class P? {issubclass(P, P)}')

main()

