from operator import imod


import random as r

def main():
    set = {r.randint(1,10) for i in range(100)}
    list =[r.randint(1,10) for i in range(100)]
    set.add(12)
    set.add(11)
    print(set)
    print(set)
    print(list)
main()
