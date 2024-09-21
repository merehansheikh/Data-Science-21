def recursive_octal(n):
    if n == 0:
        return 0
    return n%8 + 10*recursive_octal(n//8)

if __name__ == "__main__":
    for i in range(1,51):
        print(f'{i} the octal is {recursive_octal(i)}')
    # check the function through the execution or alter the loop