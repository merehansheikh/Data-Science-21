import random

def recursive_void_replace(data, height, width, sr, sc, bc, fc):
    
    if sr < 0 or sr >= height or sc < 0 or sc >= width:
        return
    
    if data[sr][sc] != bc:
        return
    
    data[sr][sc] = fc
    
    recursive_void_replace(data, height, width, sr + 1, sc, bc, fc)
    recursive_void_replace(data, height, width, sr + 1, sc + 1, bc, fc)
    
    recursive_void_replace(data, height, width, sr - 1, sc, bc, fc)
    recursive_void_replace(data, height, width, sr - 1, sc - 1, bc, fc)
    
    recursive_void_replace(data, height, width, sr, sc + 1, bc, fc)
    recursive_void_replace(data, height, width, sr - 1, sc + 1, bc, fc)
    
    recursive_void_replace(data, height, width, sr, sc - 1, bc, fc)
    recursive_void_replace(data, height, width, sr + 1, sc - 1, bc, fc)
    
    return data

def print_matrix(data):
    for row in data:
        print(row, end=' ')
        print()

if __name__ == "__main__":
    columns = 5
    rows = 3
    # mat = [[0 for i in range(columns)] for j in range(rows)]
    # for i in range(3):
    #     for j in range(3):
    #         mat[i][j]= random.randint(1, 9)
            
    mat = [
        [4,6,9,3,2],
        [6,7,2,3,1],
        [1,2,3,4,5]
    ]
    print('The matrx is: ')
    print_matrix(mat)
    print('\n')
    
    print('The matrix after replacing voids is: ')
    recursive_void_replace(mat, rows, columns, 1,2,2, 11)
    print_matrix(mat)