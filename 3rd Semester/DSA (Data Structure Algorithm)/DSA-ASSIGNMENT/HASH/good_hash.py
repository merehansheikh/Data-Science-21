

# lets assume that the value can repeat hence the value will be transferred
# to the next available location
class GoodHash:
    
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
            i = self.hash_function(val)
            while self.hash[i] != -1:
                i += 1
            self.hash[i] = val
            
        
    def hash_str(self, val):
        sum_ = 0
        for s in val:
            
            sum_ += ord(s)
        
        return sum_ % 40
    