def recursive_fibonacci_string(n):
    if n == 0:
        return 'a'
    if n == 1:
        return 'bc'
    return recursive_fibonacci_string(n-2) + recursive_fibonacci_string(n-1)

# checking the function through the main function
if __name__ == '__main__':
    print(recursive_fibonacci_string(3))
