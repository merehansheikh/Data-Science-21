

class Tree:
    def __init__(self, data, l_child = None, r_child = None) -> None:
        self.data = data
        self.left = l_child
        self.right = r_child
        
# class BinarySearchTree:
    
#     def __init__(self) -> None:
#         pass
    
    def insert(self, val):
        
        if self.data:
            
            if val < self.data:
                
                if self.left is None:
                    
                    self.left = Tree(val)
                    
                else:
                    
                    self.left.insert(val)
                    
            elif val > self.data:
                
                if self.right is None:
                    
                    self.right = Tree(val)
                    
                else:
                    
                    self.right.insert(val)
            
            else:
                
                self.data = val
          
    def search(self, val):
        
        if val < self.data:
            
            if self.left is None:
                
                return str(val) + ' Value not found'
            
            return self.left.search(val)
            
        elif val > self.data:
            
            if self.right is None:
                
                return str(val) + ' Value not found'
            
            return self.right.search(val)
            
        if val == self.data:
            
            return str(val) + ' is in the list \'hehe\' '
            
            
    def traverse_in_order(self):
        if self.left :
            self.left.traverse_in_order()
        print(self.data, end =' ')
        if self.right:
            self.right.traverse_in_order()
            
            
    def traverse_pre_order(self):
        print(self.data)
        if self.left :
            self.left.traverse()
        if self.right:
            self.right.traverse()
            
    def delete_node(self, val):
        if self.data == None:
            return
        if val < self.data:
            self.delete_node(self.left)
        elif val > self.data:
            self.delete_node(self.right)
        # No if the the value is in data the the data will be deleted
        else: 
            if self.data.left == None:
                self.data = None
            elif self.data.right == None:
                self.data = None
                
                
    
    def height(self):
        pass
            
            
            
            
  
        