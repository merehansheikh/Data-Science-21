import random


def display(x):
    for i in range(5):
        for j in range(5):
            print(x[i][j],end=' ')
        print()

def print_diagonal(x):
    for i in range(5):
        for j in range(5):
            if i == j:
                print(x[i][j], end=" ")
            else:
                print(' ', end=' ')
        print()
            
def task2():
    x=[[random.randint(11,99) for i in range(5)] for j in range(5)]
    display(x)
    print_diagonal(x)
 
task2()