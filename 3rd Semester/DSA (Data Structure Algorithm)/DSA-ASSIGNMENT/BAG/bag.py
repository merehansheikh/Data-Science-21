

# Key functions of bag are
# __init__
# insert
# remove
# set or update
# size and emptyness
# search
# iterate
# join two bags or split/trim a bag
# clone a bag
# clear or make empty a bag
import copy
class Bag:
    
    def __init__(self, arr = None) -> None:
        self.bag = arr
        if arr == None:
            self.bag = []
            self.size = 0
        else:
            self.size = len(arr) 
        
    def insert(self, val):
        
        self.bag.append(val)
        self.size += 1
        
    def remove(self, val):
        
        # rem = self.search(val)
        self.bag.remove(val)
        
    
    def search(self, val):
        self.sort()
        
        # return val in self.bag
        
        return self._binary_search(val, 0, len(self.bag) - 1)
        
        
    def _binary_search(self, val, left, right):
        
        if left > right:
            return False
        mid = (left + right) // 2
        if self.bag[mid] == val:
            return True
        elif self.bag[mid] > val:
            return self._binary_search(val, left, mid - 1)
        else:
            return self._binary_search(val, mid + 1, right)
        
    def update(self, o_val, n_val):
        if o_val in self.bag:
            self.bag[self.bag.index(o_val)] = n_val
        else:
            raise Exception('Chutti kr')
        
    def _size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def iterate(self):
        
        for ele in self.bag:
            
            print(ele, end=' ')
            
    def join(self, obj):
        
        new_obj = Bag(self.bag + obj)
        
        # new_obj.(lst)
        new_obj.bag.sort()
        return new_obj
    
    # def split(self, size):
        
    #     pass
    
    def clone(self):
        new_obj = Bag(copy.deepcopy(self.bag))
        # new_list = 
        # new_obj(new_list)
        return new_obj
    
    def empty_bag(self):
        self.bag.clear()


    def display_bag(self):
        print(self.bag)
        
        