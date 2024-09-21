from array_stack import *

class Location:
    def __init__(self, x, y):
        self.x_index = x
        self.y_index = y

    def isValidLocation(self):
        if self.x_index > -1 and self.x_index < 23 and self.y_index > -1 and self.y_index < 50:
            return True
        return False

def solveMaze(mz, starting_location):

    stk = ArrayStack()
    stk.push(starting_location)

    while not stk.isEmpty():
        lc = stk.pop()
        if mz[lc.x_index][lc.y_index] == 'E':
            break

        if mz[lc.x_index][lc.y_index] != 'S':
            mz[lc.x_index][lc.y_index] = '@'
            
        top = Location( lc.x_index - 1, lc.y_index )
        down = Location( lc.x_index + 1, lc.y_index )
        right = Location( lc.x_index, lc.y_index + 1 )
        left = Location( lc.x_index, lc.y_index - 1 )

        if (top.isValidLocation() and (mz[top.x_index][top.y_index] == ' ' or mz[top.x_index][top.y_index] == 'E')):
            stk.push(top)
        if (down.isValidLocation() and (mz[down.x_index][down.y_index] == ' ' or mz[down.x_index][down.y_index] == 'E')):
            stk.push(down)
        if (right.isValidLocation() and (mz[right.x_index][right.y_index] == ' ' or mz[right.x_index][right.y_index] == 'E')):
            stk.push(right)
        if (left.isValidLocation() and (mz[left.x_index][left.y_index] == ' ' or mz[left.x_index][left.y_index] == 'E')):
            stk.push(left)

def main():
    # maze is not a 2D list of 23 rows and 50 columns but list of 23 strings with each of len 50
    maze = [ 
        ["**************************************************"],
        ["*******                              ******** ****"],
        ["******* ************* ************** ******** ****"],
        ["******* ************* ***          * ***      ****"],
        ["        ************* **  *******  * *** **** ****"],
        ["******* *** ***    ** *  ********        **** ****"],
        ["******* *** ****** ** *  ******************** ****"],
        ["******* *** ****** **    ******************** ****"],
        ["******* *** ****** ************************** ****"],
        ["******* *** **                      ********* ****"],
        ["***     *** ** **** **** ******************** ****"],
        ["*** ********** **** ****                ***** ****"],
        ["*** ********** **** ************************* ****"],
        ["*** ********** **** ************************* ****"],
        ["***            **** ************ ************ ****"],
        ["******** ********** ************ ************ ****"],
        ["******** ********** ************      ******* ****"],
        ["********     ****** ************ **** ******* ****"],
        ["*******************              **** ******* ****"],
        ["************************************* *******S****"],
        ["************************************* ************"],
        ["*************************************            E"],
        ["**************************************************"]
        ]

    print(maze)

    for i in range(len(maze)):
        #print(i+100000)  # debugging code
        for j in range(len(maze[i])):
            #print(j)  # debugging code
            print(maze[i][j], end="")
        print()

    stLoc = Location(-1,-1)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                stLoc = Location( i, j )

    solveMaze(maze, stLoc)
    print('\n\n--------------------------------------------------------------')
    print('\n\n')
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end="")
        print()

main()