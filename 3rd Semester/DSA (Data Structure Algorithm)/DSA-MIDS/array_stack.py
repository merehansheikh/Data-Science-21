class ListStack:
    def __init__(self) -> None:
        self.l = []
        
    def push(self, val):
        self.l.append(val)
    
    def pop(self):
        return self.l.pop()
    
    def seek(self):
        self.l[-1]
    
    def printListStack(self):
        return self.l
        
class ArrayStack:
    def __init__(self, size) -> None:
        self.l = [0] * size
        self.index = 0
        
    def push(self, value):
        self.l[self.index] = value
        self.index += 1
    
    def pop(self):
        temp = self.l[self.index-1]
        self.l[self.index-1] = 0
        self.index -= 1
        return temp
    
    def seek(self):
        return self.l[self.index]
    
    def printArrayStack(self):
        i = 0
        s = ''
        while self.l[i] != 0:
            s += str(self.l[i]) + " "
            i += 1
        return s
            