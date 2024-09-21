# assuming that the class is perfect Hash and thus no repeatation is possible:


class PerfectHash:
    
    def __init__(self) -> None:
        self.hash = [-1] * 40
        
    def hash_function(self, val):
        
        if type(val) == str:
            return self.hash_str(val)
        
        return val % 40
    
    def hashing(self, val):
        if self.hash[self.hash_function(val)] != -1:
            self.hash[self.hash_function(val)] = val
        else:
            print('The location is Occupied')
        
    def hash_str(self, val):
        sum_ = 0
        for s in val:
            
            sum_ += ord(s)
        
        return sum_ % 40
    
    