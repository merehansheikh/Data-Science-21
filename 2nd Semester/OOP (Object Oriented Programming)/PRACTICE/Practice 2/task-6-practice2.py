def main():
    j =1
    k = 1
    loop = 15
    sum = 0
    for i in range(1, loop+1):
        sum+= i
        print(i ,end=' ')
        if j == k:
            print('=', sum)
            sum = 0
            k += 1
            j = 0
        j+= 1
main()