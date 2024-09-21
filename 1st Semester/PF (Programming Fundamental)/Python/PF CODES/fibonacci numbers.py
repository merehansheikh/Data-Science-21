def fibo():
    f1 = 1
    print(f1, end=", ")
    f2 = 2
    print(f2, end=", ")
    f3 = 5
    print(f3, end=", ")
    f = f1 + f2 + f3

    while f <= 100000000:
        print(f, end=", ")
        f1 = f2
        f2 = f3
        f3 = f
        f = f1 + f2 + f3
fibo()
