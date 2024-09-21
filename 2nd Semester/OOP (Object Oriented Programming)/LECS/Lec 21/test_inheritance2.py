class P:
    def __init__(self):
        print('Init function from parent is called')

    def check(self):
        print('Check function from parent class is called')

class C(P):
    def __init__(self):
        print('Init function from child is called')

def main():
    object = C()
    object.check()

main()

