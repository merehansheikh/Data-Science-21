def cube(n):
    return n**3

def main():
    n = int(input("Input number of terms: "))
    for i in range(1,n+1):
        print('number is:', i, 'and the cube of', i, 'is', cube(i))

main()