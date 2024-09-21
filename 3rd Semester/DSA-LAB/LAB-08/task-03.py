class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, node):
        if self.head is None:
            return
        elif self.head == node:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current != node:
                prev = current
                current = current.next
            prev.next = current.next

    def print_list(self):
        if self.head is None:
            return
        current = self.head
        print(current.data, end=" ")
        while current.next != self.head:
            current = current.next
            print(current.data, end=" ")
        print()

    def get_survivor(self, k):
        current = self.head
        while current.next != current:
            for i in range(k-1):
                current = current.next
            next_node = current.next
            self.delete(current)
            current = next_node
        return current.data


# implementation
if __name__ == '__main__':
    n = 7
    k = 3
    people = LinkedList()
    for i in range(1, n+1):
        people.insert(i)
    print("Initial circle:")
    people.print_list()
    survivor = people.get_survivor(k)
    print("Survivor:", survivor)
