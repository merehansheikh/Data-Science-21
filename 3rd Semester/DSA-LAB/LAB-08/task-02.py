class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedListNode:
    
            
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def append(self, data):
        node = Node(data)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
    def remove(self, data):
        node = self.head.next
        while node is not self.tail:
            if node.data == data:
                node.prev.next = node.next
                node.next.prev = node.prev
                break
            node = node.next
        
    def __len__(self):
        node = self.head.next
        count = 0
        while node is not self.tail:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        node = self.head.next
        while node is not self.tail:
            yield node.data
            node = node.next



# implementation of the doubly linked lis
if __name__ == '__main__':
    
    obj = DoublyLinkedListNode()
    obj.append(1)
    obj.append(2)
    obj.append(3)
    obj.append(4)
    obj.append(5)
    obj.append(6)
    obj.append(7)
    obj.append(8)
    obj.append(9)
    obj.append(10)
 
    
    myIter = iter(obj)
    
    for obj in myIter:
        print(obj)

