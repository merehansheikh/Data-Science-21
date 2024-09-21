def lcm(a,b):
    if a > b:
        grt = a
    else:
        grt = b
    while grt <= (a * b):
        if(grt%a==0) and (grt%b==0):
            lcm = grt
            break
        grt = grt + 1
    return lcm

def main():
    q = int(input())
    w = int(input())
    print(lcm(q,w))
main()