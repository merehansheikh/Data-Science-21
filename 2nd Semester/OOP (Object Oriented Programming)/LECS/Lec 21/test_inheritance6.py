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
    print (f'Is object_c is instance/ object of class C? {isinstance(object_c, C)}')
    print (f'Is object_c is instance/ object of class P? {isinstance(object_c, P)}')
    print (f'Is object_c is instance/ object of class Dummy? {isinstance(object_c, Dummy)}')
    print (f'Is object_p is instance/ object of class C? {isinstance(object_p, C)}')
    print (f'Is object_p is instance/ object of class P? {isinstance(object_p, P)}')

main()

