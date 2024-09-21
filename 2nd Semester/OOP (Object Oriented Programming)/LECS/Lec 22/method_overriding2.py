class P:
    def f1(self):
        print ('F1 of P')
    def f2():
        print ('F2 of P')

class C(P):
    def f1(self, x):
        print ('F1 of C')

def main():
    object_c = C()
    object_p = P()
    object_p.f1()
    #object_c.f1()
    object_c.f1(5)

main()

