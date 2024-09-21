ans = 0

def func(n):
    if n == 1:
        return
    
    global ans
    for i in range(int(n*n)):
        ans += 1
        
    func(n//2)
    func(n//2)
    return ans
    
for i in range(50000, 50001):
    ans = 0
    func(i)
    print(i, ans)