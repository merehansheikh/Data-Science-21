from array_stack import *

def void_replace(data, height, width, sr, sc, bc, fc):
    stack = ArrayStack()
    # indeces 
    i = sr
    j = sc
    # pushing the indeces as a list
    stack.push([sr, sc])
    while not stack.isEmpty():
        # poping from the stack 
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

