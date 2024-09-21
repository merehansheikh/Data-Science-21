from abc import ABC, abstractmethod
class Queue(ABC):
    
    @abstractmethod
    def __init__(self): pass
    @abstractmethod
    def enqueue(self): pass
    @abstractmethod
    def dequeue(self): pass
    @abstractmethod
    def peek(self): pass
    @abstractmethod
    def __iter__(self): pass
    @abstractmethod
    def __next__(self): pass
    
    