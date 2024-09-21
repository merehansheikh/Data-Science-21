from copy import deepcopy
import time


def find_index(init_state):
    for i in range(3):
        try:
            j_ind = init_state[i].index(0)
            i_ind = i
        except:
            pass
    return i_ind, j_ind


def move(state, last_i, last_j, i, j):
    try:
        state[last_i][last_j], state[i][j] = state[i][j], state[last_i][last_j]

        return state
    except:
        pass


def dfs(init_state, goal_state):
    visited.append(init_state)

    if init_state == goal_state:
        print("Path Found")
        return goal_state
    i, j = find_index(init_state)
    c = deepcopy(init_state)
    if i < 0 or j < 0 or i >= 3 or j >= 3:
        return

    # for down
    if i < 3 and j < 3 and i >= 0 and j >= 0:
        s = move(c, i, j, i + 1, j)

        if s != None and s not in visited:
            # if init_state not in visited:
            v = dfs(s, goal_state)

            if v != None:
                return init_state + v
    # for left
    if i < 3 and j < 3 and i >= 0 and j >= 0:
        s = move(c, i, j, i, j - 1)

        # if init_state not in visited:
        if s != None and s not in visited:
            v = dfs(s, goal_state)
            if v != None:
                return init_state + v

    # for up
    if i < 3 and j < 3 and i >= 0 and j >= 0:
        s = move(c, i, j, i - 1, j)

        # if init_state not in visited:
        if s != None and s not in visited:
            v = dfs(s, goal_state)
            if v != None:
                return init_state + v

    # for right
    if i < 3 and j < 3 and i >= 0 and j >= 0:
        s = move(c, i, j, i, j + 1)

        # if init_state not in visited:
        if s != None and s not in visited:
            v = dfs(s, goal_state)
            if v != None:
                return init_state + v


if __name__ == "__main__":
    state = [[1, 0, 2], [4, 5, 3], [7, 8, 6]]

    final_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    visited = []

    # print(i, j)

    l = dfs(state, final_state)
    print(l)
