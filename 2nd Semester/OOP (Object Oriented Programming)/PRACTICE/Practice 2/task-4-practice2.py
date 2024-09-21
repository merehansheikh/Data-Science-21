def main():
    j =1
    k = 1
    loop = 10
    sum = 0
    for i in range(1, loop+1):
        print(i ,end=' ')
        if j == k:
            print()
            k += 1
            j = 0
        j+= 1
main()