from LinkedStack import *

def void_replace(data, height, width, sr, sc, bc, fc):
    stack = LinkedStack()
    i = sr
    j = sc
    stack.push([sr, sc])
    while not stack.isEmpty():
        x = stack.pop()
        if x[0] < len(data) and x[1] < len(data[0]):
            if data[x[0]][x[1]] == bc:
                data[x[0]][x[1]] = fc
                stack.push((x[0]-1, x[1]-1))
                stack.push((x[0] - 1, x[1]))
                stack.push((x[0] - 1, x[1] + 1))
                stack.push((x[0] + 1, x[1] - 1))
                stack.push((x[0] + 1, x[1]))
                stack.push((x[0] + 1, x[1] + 1))
                stack.push((x[0], x[1] + 1))
                stack.push((x[0], x[1] - 1))


def print_list(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            print(lst[i][j], end=" ")
        print()

def main():
    lst = [
        [1,1,1,1,1,2,1,1,2],
        [2,2,8,2,2,2,2,1,1],
        [2,8,8,2,2,5,7,8,2],
        [2,8,8,2,9,2,2,8,3],
        [4,4,0,2,9,2,6,2,2],
        [0,4,2,2,9,2,2,2,5],
        [9,4,2,2,2,2,2,2,4],
        [0,4,4,4,4,4,5,4,4]
    ]
    print_list(lst)
    print("#################")
    # (data, height, width, sr, sc, bc, fc)
    void_replace(lst, 8, 9, 3, 5, 2, 11)
    print_list(lst)
main()

