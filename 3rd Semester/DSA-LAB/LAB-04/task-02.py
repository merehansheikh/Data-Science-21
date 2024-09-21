from abc import ABC, abstractmethod
import random
class MatrixADT(ABC):
    @abstractmethod
    def __init__(self, rows, columns):
        pass
    
    @abstractmethod
    def set_element(self, row, column, value):
        pass
    
    @abstractmethod
    def print_matrix(self):
        pass
    
    @abstractmethod
    def sum_matrix(self):
        pass
    
    @abstractmethod
    def add_matrix(self, matrix):
        pass
    @abstractmethod
    def transpose(self):
        pass
    
    @abstractmethod
    def order(self):
        pass
    
    @abstractmethod
    def is_square(self):
        pass
    
    @abstractmethod
    def is_symmetric(self):
        pass
    
    @abstractmethod
    def diagonal_sum(self):
        pass
class Matrix(MatrixADT):
    
    def __init__(self,rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for i in range(columns)] for j in range(rows)]
        
    def set_element(self, row, column, value):
        self.matrix[row][column] = value
        
    def print_matrix(self):
        for row in self.matrix:
            print(row, end=' ')
            print()
    
    def sum_matrix(self):
        return sum([sum(row) for row in self.matrix])
    
    def add_matrix(self, matrix):
        if self.rows == matrix.rows and self.columns == matrix.columns:
            new_obj =Matrix(self.rows, self.columns)
            new_obj = [[self.matrix[i][j] + matrix.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
            return new_obj
        else:
            return 'Matrices are not of same size'
    
    def transpose(self):
        return [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.columns)]
    
    def order(self):
        return (self.rows, self.columns)
    
    def is_square(self):
        return self.rows == self.columns
    
    def is_symmetric(self):
        return self.matrix == self.transpose()
    
    def diagonal_sum(self):
        return sum([self.matrix[i][i] for i in range(self.rows)])
    
    
if __name__ == '__main__':
    # creating a matrix1
    matrix1 = Matrix(3, 3)
    for i in range(3):
        for j in range(3):
            matrix1.set_element(i, j, random.randint(1, 9))
    print('Matrix 1: ')
    matrix1.print_matrix()
    print('\n')
    
    matrix2 = Matrix(3, 3)
    for i in range(3):
        for j in range(3):
            matrix2.set_element(i, j, random.randint(1, 9))
    print('Matrix 2: ')
    matrix2.print_matrix()
    print('\n')
    
    # sum of all elements in a matrix
    print('Sum of all elements in matrix1: ', end=' ')
    print(matrix1.sum_matrix())
    print('\n')
    
    # addition of two matrices
    print('Addition of matrix1 and matrix2: ')
    print(matrix1.add_matrix(matrix2))
    print('\n')
    
    # transpose of a matrix
    print('Transpose of matrix1: ')
    print(matrix1.transpose())
    print('\n')
    
    # order of a matrix
    print('Order of the matrix :', end = ' ')
    print(matrix1.order())
    print('\n')
    
    # checking whethet the matrix is square or not
    print('Is matrix1 square? ')
    print(matrix1.is_square())
    print('\n')
    
    # checking whether the matrix is symmetric or not
    print('Is matrix1 symmetric?')
    print(matrix1.is_symmetric())
    print('\n')
    
    # printing the sum of diagonal elements
    print('Diagonal sum of matrix1:')
    print(matrix1.diagonal_sum())
    print('\n')
    