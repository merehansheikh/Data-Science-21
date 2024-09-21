import numpy


def karatsuba(x, y):
    
    if x < 10 or y< 10:
        return x * y
    
    else:
        
        n = max(len(str(x)) , len(str(y)))
        
        half = n//2
        
        a = x // (10 ** (half)) # left part of X
        b = x % (10 ** (half)) # right part of x
        
        c = y // (10 ** (half)) #left part of Y
        d = y % (10 ** (half)) # right part of x
        
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a+b, c+d) - ac - bd
        
        return (ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd)
    
    
if __name__ == "__main__":
    a = 12345678900987654321234567890098765432112
    b = 1234563456785678098765678987656712345634567
    print(a*b) 
    print()
    print()
    print(karatsuba(a,b))
    