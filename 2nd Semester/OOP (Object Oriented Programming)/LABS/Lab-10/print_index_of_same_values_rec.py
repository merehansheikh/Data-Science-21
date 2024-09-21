import random as r
def print_index_of_same_values(x, i=0, j=1):
    if i==len(x):   return
    if j<len(x):
        if x[i] == x[j]:    print (f'({i}, {j})')
        print_index_of_same_values(x, i, j+1)
    else:
        print_index_of_same_values(x, i+1, i+2)

def main():
    x = [r.randint(1,5) for i in range(10)]
    print(x)
    print_index_of_same_values(x)

main()