def check_perfect_square(num):
    i = 2
    while i < num:
        if i**2 == num:
            return True
        i += 1
    return False

def main():
    d = [2, 4, 6, 9, 25]
    count = 0
    for i in range(len(d)):
        if check_perfect_square(d[i]):
            count += 1
    print(count)

main()