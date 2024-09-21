from copy import deepcopy
import time


def dfs(initial_state, goal_state, visited):
    if initial_state == goal_state:
        print("Solution Found")

        return goal_state

    ind = index_empty(initial_state)
    i = ind[0]
    j = ind[1]

    for pos in [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]:
        li = deepcopy(initial_state)

        new_pos = (i + pos[0], j + pos[1])

        if 0 <= new_pos[0] <= 2 and 0 <= new_pos[1] <= 2:
            li[i][j] = li[new_pos[0]][new_pos[1]]
            li[new_pos[0]][new_pos[1]] = 0

            if li not in visited:
                visited.append(li)

                v = dfs(li, goal_state, visited)
                if v != None:
                    return initial_state + v


def display_puzzle(li):
    count = 0
    for i in li:
        if count == 3:
            count = 0
            print()
            print()

        print(i)
        count += 1


def index_empty(li):
    for i in range(len(li)):
        for j in range(3):
            if li[i][j] == 0:
                return (i, j)


def main():
    # initial_state =[[2,3,6],
    #                 [1,5,0],
    #                 [4, 7,8]]
    # goal_state =[[1,2,3],
    #              [4,5,6],
    #              [7,8,0]]
    initial_state = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]

    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    visited = [initial_state]
    v = dfs(initial_state, goal_state, visited)
    if v == None:
        print("No Solution exist")
    else:
        display_puzzle(v)


main()
