import random


def display(x):
    for i in range(5):
        for j in range(5):
            print(x[i][j],end='    ')
        print()

def print_sum_column(x):
    sum_column  = [0]* 5
    for i in range(5):
        for j in range(5):
            sum_column[j] += x[i][j]
    for i in range(len(sum_column)):
        print(sum_column[i], end='   ')
        
def main():
    x=[[random.randint(11,99) for i in range(5)] for j in range(5)]
    display(x)
    print()
    print_sum_column(x)
 
main()