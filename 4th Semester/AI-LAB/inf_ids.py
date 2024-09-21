from copy import deepcopy


def get_poistion(tile, state):
    for i in range(len(state[0])):
        for j in range(len(state[0])):
            if state[i][j] == tile:
                return i, j


def manhattan_distance(current_state, goal_state, distance=0):
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if current_state[i][j]:
                row, col = get_poistion(current_state[i][j], current_state)
                goal_row, goal_col = get_poistion(goal_state[i][j], goal_state)
                distance += abs(row - goal_row) + abs(col - goal_col)
    return distance


def ids(depth, state, i, j, goal_state, visited):
    if state == goal_state:
        print(f"Number of Visited States {len(visited)} \n")
        return True

    if state in visited:
        return False

    if not depth:
        return "Limit Reached"

    visited.append(state)

    manhattan_heuristic_list = list()
    for depth_i, depth_j in (
        (1, 0),  # ->FOR BOTTOM
        (-1, 0),  # -> FOR TOP
        (0, 1),  # -> FOR RIGHT
        (0, -1),  # -> FOR LEFT
    ):
        temp_state = deepcopy(state)

        if 0 <= i + depth_i < len(temp_state) and 0 <= j + depth_j < len(temp_state[0]):
            temp_state[i][j], temp_state[i + depth_i][j + depth_j] = (
                temp_state[i + depth_i][j + depth_j],
                temp_state[i][j],
            )
            manhattan_val = manhattan_distance(temp_state, goal_state)
            manhattan_heuristic_list.append(
                [manhattan_val, temp_state, i + depth_i, j + depth_j]
            )

    manhattan_heuristic_list = sorted(manhattan_heuristic_list, key=lambda x: x[0])
    for _, state, i, j in manhattan_heuristic_list:
        answer = ids(depth - 1, state, i, j, goal_state, visited)
        if answer == True:
            display(state)
            return True


def display(state):

    for i in state:
        print(i)
    print("\n")

    # print(len(state))


def find_zero_index(state):

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


if __name__ == "__main__":

    initial_state = [[1, 3, 6], [2, 7, 0], [4, 5, 8]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    d = 1
    index = find_zero_index(initial_state)
    i, j = index[0], index[1]

    while True:
        ans = ids(d, initial_state, i, j, goal_state, list())
        if ans == True:
            print("Path Found")
            break
        d += 1
