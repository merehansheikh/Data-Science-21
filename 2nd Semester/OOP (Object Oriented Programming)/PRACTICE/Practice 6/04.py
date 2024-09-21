import random

def display(x):
    for i in range(5):
        for j in range(5):
            print(x[i][j],end=' ')
        print()

def print_triangle(x):
    j = 0
    for i in range(5):
        print('   '* j,end='')
        while j < 5:
            print(x[i][j], end=' ')
            j += 1
        j = 0
        j = i+1
        print()
        
def main():
    x=[[random.randint(11,99) for i in range(5)] for j in range(5)]
    display(x)
    print()
    print_triangle(x)
 
main()