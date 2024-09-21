def funcsum(a, b, c):
    sum = a + b+ c
    return sum
def funcavrg(a, b):
    return a / b
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    sum = funcsum(a, b, c)
    avrg = funcavrg(sum, 3)
    print(avrg)
main()

