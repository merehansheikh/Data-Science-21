class ArrayStack():
    def __init__(self, size= 1000):
        self.size = size
        self.stack = [-1] * self.size
        self.index = 0
        self.top = 0
        
    def push(self, item):
        if self.index == self.size:
            raise Exception("Stack is full")
        else:
            self.stack[self.index] = item
            self.index += 1
            self.top += 1
    
    def pop(self):
        if self.index != 0:
            self.index -= 1
            self.top -= 1
            temp = self.stack[self.top]
            
            return temp
        else:
            raise Exception("Stack is empty")
    
    def isEmpty(self):
        return self.index == 0  
    
    def isFull(self):
        return self.idex == self.size
    
    def __str__(self):
        return str(self.stack[0:self.index])
    
