import random


def display(x):
    for i in range(5):
        for j in range(5):
            print(x[i][j],end=' ')
        print()

def sum_of_row(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return sum

def print_sum_of_row(x):
    row = 1
    for i in range(len(x)):
        sum = sum_of_row(x[i])
        print(f'Sum of row {row}: {sum}')
        row += 1
        
def main():
    x=[[random.randint(11,99) for i in range(5)] for j in range(5)]
    display(x)
    print()
    print_sum_of_row(x)
    
 
main()