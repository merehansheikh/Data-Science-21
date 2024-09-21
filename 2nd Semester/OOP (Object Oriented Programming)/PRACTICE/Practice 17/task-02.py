class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0
    
    def set_length(self, length):
        self.length = length
    
    def set_width(self, width):
        self.width = width
    
    def display(self):
        return (f"The rectangle has {self.length}cm of length and {self.width}cm of width ")
    
class Block(Rectangle):
    def __init__(self):
        super().__init__()
        self.height = 0
    
    def set_height(self, height):
        self.height = height
    
    def display(self):
        print(f"{Rectangle.display(self)} and now {self.height}cm of height.")

def main():
    obj = Block()
    obj.set_length(12)
    obj.set_width(69)
    obj.set_height(69)
    obj.display()
main()
