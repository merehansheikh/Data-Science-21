class DoublyLinkedList:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
        
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def append(self, data):
        node = self.Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            
    def pop(self):
        if self.head is None:
            return None
        else:
            node = self.tail
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = node.prev
                self.tail.next = None
            return node.data        
    
    def remove(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                break
            node = node.next        
    
    def add_before(self, data, new_data):
        node = self.head
        while node is not None:
            if node.data == data:
                new_node = self.Node(new_data)
                new_node.next = node
                new_node.prev = node.prev
                if node.prev is not None:
                    node.prev.next = new_node
                else:
                    self.head = new_node
                node.prev = new_node
                break
            node = node.next
    def add_after(self, data, new_data):
        node = self.head
        while node is not None:
            if node.data == data:
                new_node = self.Node(new_data)
                new_node.next = node.next
                new_node.prev = node 
                if node.next is not None:
                    node.next.prev = new_node
                else:
                    self.tail = new_node
                node.next = new_node
                break
            node = node.next
    
    def print(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
            
    def print_reverse(self):
        node = self.tail
        while node is not None:
            print(node.data)
            node = node.prev