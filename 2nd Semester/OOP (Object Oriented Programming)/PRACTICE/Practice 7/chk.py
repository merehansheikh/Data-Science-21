def armstrong_num(n):
    st = str(n)
    sum = 0
    for i in range(len(st)):
        sum += int(st[i]) **3
    if sum ==n:
        return True
    return False
def main():
    n = int(input('Enter the number you want to check: '))
    if armstrong_num(n):
        print('Yes')
    else:
        print('No')

main()
