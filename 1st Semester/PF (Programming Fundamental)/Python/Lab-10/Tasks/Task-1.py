class Matrix:
    pass


def createMatrix(rows, cols):
    m = Matrix()
    m.RowCount = rows
    m.ColumnCount = cols
    m.Data = [[0 for c in range(cols)] for r in range(rows)]
    return m


def inputMatrix(m):
    i = 0
    while i < m.RowCount:
        j = 0
        while j < m.ColumnCount:
            m.Data[i][j] = int(input())
            j += 1
        i += 1
    return


def printMatrix(m):
    i = 0
    while i < m.RowCount:
        j = 0
        while j < m.ColumnCount:
            print(m.Data[i][j], end=" ")
            j += 1
        print()
        i += 1
    return

def transposeMatrix(m):
    t = createMatrix(m.ColumnCount, m.RowCount)

    i = 0
    while i < t.RowCount:
        j = 0
        while j < t.ColumnCount:
            t.Data[i][j] = m.Data[j][i]
            j += 1
        i += 1
    return t

def addMatrices(m1, m2):
    if m1.RowCount != m2.RowCount or m1.ColumnCount != m2.ColumnCount:
	    raise "Only matrices with same order can be added"

    r = createMatrix(m1.RowCount, m1.ColumnCount)

    i = 0
    while i < r.RowCount:
        j = 0
        while j < r.ColumnCount:
            r.Data[i][j] = m1.Data[i][j] + m2.Data[i][j]
            j += 1
        i += 1
    return r

def isSymmetric(m):
    if m.RowCount != m.ColumnCount:
	    raise "Not a Square Matrix, Only a Square Matrix be Symmetric"

    i = 0
    while i < m.RowCount:
        j = 0  # j can be set here to i+1
        while j < m.ColumnCount:
            if m.Data[i][j] != m.Data[j][i]:
                return False
            j += 1
        i += 1
    return True

def main():
    two2_1 = createMatrix(2, 2)
    print("Enter 4 intgers for a 2 X 2 Matrix")
    inputMatrix(two2_1)
    print("The entered Matrix is")
    printMatrix(two2_1)
    print()

    two2_2 = createMatrix(2, 2)
    print("Enter 4 intgers for a 2 X 2 Matrix")
    inputMatrix(two2_2)
    print("The entered Matrix is")
    printMatrix(two2_2)
    print()

    print("Enter a matrix you want to check is symmetric or not")
    rows_sym = int(input("Enter rows:"))
    cols_sym = int(input("Enter columns:"))
    sym_matrix = createMatrix(rows_sym, cols_sym)
    print("Enter integers for the matrix")
    inputMatrix(sym_matrix)
    symmetric = isSymmetric(sym_matrix)
    if symmetric == True:
        print("The matrix is symmetric")
    else:
        print("The matric is unsymmetric.")
    print()

    print("Enter a matrix you want to ADD")
    rows_add = int(input("Enter rows:"))
    cols_add = int(input("Enter columns:"))
    add_matrix_1 = createMatrix(rows_add, cols_add)
    add_matrix_2 = createMatrix(rows_add, cols_add)
    print("Enter the integers for the 1st matrix")
    inputMatrix(add_matrix_1)
    print("Enter the integers for the 2nd matrix")
    inputMatrix(add_matrix_2)
    added_matrix = addMatrices(add_matrix_1, add_matrix_2)
    print("The addition of matrices is:")
    printMatrix(added_matrix)
    print()

    three2 = createMatrix(3, 2)
    print("Enter 6 intgers for a 3 X 2 Matrix")
    inputMatrix(three2)
    print("The entered Matrix is")
    printMatrix(three2)
    print()
    two3 = transposeMatrix(three2)
    print("The transpose of above Matrix is")
    printMatrix(two3)
    print()

main()
