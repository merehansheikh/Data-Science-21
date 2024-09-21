def recursive_sum_over(n):
    if n == 1: return 1
    return 1/n * recursive_sum_over(n-1)

# execution through the main function
if __name__ == '__main__':
    print(recursive_sum_over(3))