def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def recursive_ex(x, k):
    if k == 1:
        return 1
    return (x ** (k-1)/factorial(k-1)) + recursive_ex(x, k-1)

if __name__ == '__main__':
    print(factorial(5)) #checking the factorial function
    print(recursive_ex(1, 3)) #checking the recursive_ex function
