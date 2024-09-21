def main():
    f = open('practice8.txt', 'r')
    r = f.read()

    for letters in r:
        if ord(letters) >= ord('0') and ord(letters) <=ord('9'):
            print(letters)
    f.close()
main()