class LinkedStack:

    def __init__(self):
        self._top = None
        self._count = 0

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def count(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        raise NotImplementedError("isFull is not implemented as in-approprite for Linked Nodes")

    def push(self, val):
        tmp = self.Node(val)
        if not self.isEmpty():
            tmp.next = self._top
        self._top = tmp
        self._count = self._count + 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack empty")
        else:
            tmp = self._top
            self._top = tmp.next
            tmp.next = None
            self._count = self._count - 1
            return tmp.data


def replace(data, height, width, sr, sc, bc, fc):
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
    replace(lst, 8, 9, 3, 5, 2, 11)
    print_list(lst)
main()

