from random import randint

def populate(arr, columns, rows, dimension_3):
    i = 0
    while i < dimension_3:
        r = 0
        while r < rows:
            c = 0
            while c < columns:
                arr[i][r][c] = randint(11,99)
                c += 1
            r += 1
        i += 1
    return(arr)

def print_2D_arr(arr, dimension_3rd):
    i = 0
    while i < dimension_3rd:
        print(arr[i])
        i += 1

def main_1():

    rows = 9
    columns = 7
    dimension_3 = 4
    arr = [[[0 for i in range(columns)]for i in range(rows)]for i in range(dimension_3)]
    arr = populate(arr, columns, rows, dimension_3)
    print_2D_arr(arr, dimension_3)

main_1()