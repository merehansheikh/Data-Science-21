from perfect_hash import *
def hash_str(val):
        sum_ = 0
        for s in val:
            
            sum_ += ord(s)
        
        return sum_ % 40

if __name__ == '__main__':
    while True:
        
        t = input()
        if t == -1:
            break
        if type(t) == str:
            print(t, hash_str(t))
        else:
            print(t, int(t)%40)
        
        