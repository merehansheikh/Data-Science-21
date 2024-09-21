class P:
    def f(self):
        print ('abc')

class C(P):
    def f(self):
        print ('def')


def main():
    object_c = C()
    object_p = P()
    object_p.f()
    object_c.f()

main()

