# linked nodes based code for implementation of LIST basics
class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    class LLIterator:
        def __init__(self, node):
            self.current = node

        def __next__(self):
            cur_node = self.current
            if self.current != None:
                self.current = self.current.next
            else:
                raise StopIteration
            return cur_node.data

    def __iter__(self):
        return self.LLIterator(self.head)

    def append(self, o):
        if self.head == None:
            self.head = self.Node(o)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = self.Node(o)

    def Display(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next
        print()


def main():
    # Create a new Linked List
    ll = LinkedList()
    # Insert elements to empty list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(70)
    ll.append(50)
    ll.append(60)
    ll.append(80)
    ll.append(90)
    ll.append(40)

    # Display Data
    print("Display 10 items")
    ll.Display()

    print("OUTPUT of 'for d in ll:'")
    for d in ll:
        print(d)
    print()

main()
