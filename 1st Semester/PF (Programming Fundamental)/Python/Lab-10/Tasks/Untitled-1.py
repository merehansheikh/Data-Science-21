class Matrix:
    pass
def createMatrix(rows,cols):
    m = Matrix()
    m.Rowcount = rows
    m.Colcount = cols
    m.arr = [[0 for i in range(cols) ]for i in range(rows)]
    return m
def inputMatrix(m):
    i = 0
    while i < m.Rowcount:
        j = 0
        while j < m.Colcount:
            m.arr[i][j] = int(input())
            j = j+1
        i = i + 1
    return m
def printMatrix(m):
    i = 0
    while i<m.Rowcount:
        j = 0
        while j <m.Colcount:
            print(m.arr[i][j],end = " ")
            j = j + 1
        print()
        i = i + 1
    return m
def main():
    a = createMatrix(4,5)
    inputMatrix(a)
    printMatrix(a)
main()

    