def check_perfect_cube(num):
    i = 2
    while i < num:
        if i**3 == num:
            return True
        i += 1
    return False

def main():
    d = [2, 4, 8, 9, 25]
    count = 0
    for i in range(len(d)):
        if check_perfect_cube(d[i]):
            count += 1
    print(count)

main()