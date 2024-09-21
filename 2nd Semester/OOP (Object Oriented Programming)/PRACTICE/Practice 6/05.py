import random


def display(x):
    for i in range(5):
        for j in range(5):
            print(x[i][j],end=' ')
        print()


def print_triangle(x):
    
    rng =5
    for i in range(5):
        j = 0
        while j < rng:
            print(x[i][j], end=' ')
            j += 1
        rng -= 1
        print()
        
def main():
    x=[[random.randint(11,99) for i in range(5)] for j in range(5)]
    display(x)
    print()
    print_triangle(x)
 
main()