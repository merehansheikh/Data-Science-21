import random

def rand():
    a = random.randint(1,99)
    return a

def main():
    a = rand()
    b = rand()
    c = rand()
    d = rand()

    print (a," ",b," ",c," ",d)

    if a<=b:
        if b<=c:
            if c<=d:
                print (a," ",b," ",c," ",d)
    if a<=b:
        if b<=d:
            if d<=c:
                print (a," ",b," ",d," ",c)
    if a<=c:
        if c<=b:
            if b<=d:
                print (a," ",c," ",b," ",d)
    if a<=c:
        if c<=d:
            if d<=b:
                print (a," ",c," ",d," ",b)
    if a<=d:
        if d<=c:
            if c<=b:
                print (a," ",d," ",c," ",b)
    if a<=d:
        if d<=b:
            if b<=c:
                print (a," ",d," ",b," ",c)

    
    if b<=a:
        if a<=c:
            if c<=d:
                print (b," ",a," ",c," ",d)
    if b<=a:
        if a<=d:
            if d<=c:
                print (b," ",a," ",d," ",c)
    if b<=c:
        if c<=a:
            if a<=d:
                print (b," ",c," ",a," ",d)
    if b<=c:
        if c<=d:
            if d<=a:
                print (b," ",c," ",d," ",a)
    if b<=d:
        if d<=c:
            if c<=a:
                print (b," ",d," ",c," ",a)
    if b<=d:
        if d<=a:
            if a<=c:
                print (b," ",d," ",a," ",c)


    if c<=a:
        if a<=b:
            if b<=d:
                print (c," ",a," ",b," ",d)
    if c<=a:
        if a<=d:
            if d<=b:
                print (c," ",a," ",b," ",d)
    if c<=b:
        if b<=a:
            if a<=d:
                print (c," ",b," ",a," ",d)
    if c<=b:
        if b<=d:
            if d<=a:
                print (c," ",b," ",d," ",a)
    if c<=d:
        if d<=a:
            if a<=b:
                print (c," ",d," ",a," ",b)
    if c<=d:
        if d<=b:
            if b<=a:
                print (c," ",d," ",b," ",a)


    

    if d<=a:
        if a<=b:
            if b<=c:
                print (d," ",a," ",b," ",c)
    if d<=a:
        if a<=c:
            if c<=b:
                print (d," ",a," ",c," ",b)
    if d<=b:
        if b<=a:
            if a<=c:
                print (d," ",b," ",a," ",c)
    if d<=b:
        if b<=c:
            if c<=a:
                print (d," ",b," ",c," ",a)
    if d<=c:
        if c<=a:
            if a<=b:
                print (d," ",c," ",a," ",b)
    if d<=c:
        if c<=b:
            if b<=a:
                print (d," ",c," ",b," ",a)

main()