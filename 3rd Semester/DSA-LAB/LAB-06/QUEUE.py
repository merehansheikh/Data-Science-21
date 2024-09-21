from abc import ABC, abstractmethod


# class Queue(ABC):
    
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def enqueue(self, item):
#         pass
    
#     @abstractmethod
#     def dequeue(self, item):
#         pass
    
#     @abstractmethod
#     def is_empty(self):
#         pass
    
#     @abstractmethod
#     def size(self):
#         pass
    
    
class Queue:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def enqueue(self, item):
        if self.head == None:
            self.head = self.Node(item)
            self.tail = self.head
        else:
            self.tail.next = self.Node(item)
            self.tail = self.tail.next
        self.count += 1
        
    def dequeue(self):
        if self.head == None:
            raise Exception("Queue is empty")
        else:
            tmp = self.head
            self.head = self.head.next
            self.count -= 1
            return tmp.data
        
    def is_empty(self):
        return self.count == 0
    
    
    def size(self):
        return self.count
    
    def peek(self):
        if self.head == None:
            raise Exception("Queue is empty")
        else:
            return self.head.data
        
    def is_empty(self):
        return self.count == 0
    
    def size(self):
        return self.count
    