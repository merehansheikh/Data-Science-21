def recursive_hcf(a,b):
    if b == 0:
        return a
    return recursive_hcf(b, a%b)
# checking the function through the execution
if __name__ == "__main__":
    print(recursive_hcf(120, 168))