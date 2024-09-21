class P:
    def __init__(self):
        print('Init function from parent is called')

class C(P):
    def __init__(self):
        print('Init function from child is called')

def main():
    object = C()

main()
