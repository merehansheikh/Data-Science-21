def recursive_sum(n):
    if n == 0:
        return 0
    return n%10 + recursive_sum(n//10)
    
# if __name__ == '__main__':
print(recursive_sum(16))
print(recursive_sum(1234))
# for checking the function