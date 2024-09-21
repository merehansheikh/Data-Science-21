def main():
    f = open('practice8.txt', 'r')
    r = f.read()
    sum = 0
    for letters in r:
        if ord(letters) >= ord('0') and ord(letters) <=ord('9'):
            sum += 1
    print(sum)
    f.colse()
main()