import random


def display(x):
    for i in range(5):
        for j in range(5):
            print(x[i][j],end=' ')
        print()

def chk_max_and_index(x):
    max = x[0]
    index = 0
    for i in range(len(x)):
        if x[i] > max:
            max = x[i]
            index = i
    return max, index

def print_max_index(x):
    row = 1
    for i in range(len(x)):
        max, index = chk_max_and_index(x[i])
        print(f'Row {row}: {max} is at index {index}')
        row += 1
        
def main():
    x=[[random.randint(11,99) for i in range(5)] for j in range(5)]
    display(x)
    print()
    print_max_index(x)
    
 
main()