def MUL(x,y,n):
    if n == 1:
        return x*y
    
    m = int(n/2)
    zeros = 10**m
    
    xl = int(x / zeros)
    xr = x - xl * zeros
    yl = int(y / zeros)
    yr = y - yl*zeros
    
    xlyl = MUL(xl, yl, m)
    xlyr = MUL(xl, yr, m)
    xryl = MUL(xr, yl, m)
    xryr = MUL(xr, yr, m)
    
    return xlyl*(zeros**2) + (xlyr+xryl)*zeros + xryr
  
def main():
    num1 = 73624239617454239617455926096592
    num2 = 23737362423961745592624239961745
    res = MUL(num1, num2, 32)
    print(num1*num2)
    print(res)

main()

  