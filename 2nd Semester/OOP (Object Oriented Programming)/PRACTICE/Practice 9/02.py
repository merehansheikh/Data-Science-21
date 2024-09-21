import random


def main():
    # l = [[1,2,3],[4,5,6],[7,8,9]]
    l = [[random.randint(1,9) for i in range(3)] for i in range(3)]
    print(l)
    len_col = 2
    while len_col >= 0:
        lent_row = 2
        while lent_row >= 0:
            print(l[len_col][lent_row], end=' ')
            lent_row -= 1
        print()
        len_col-= 1

main()