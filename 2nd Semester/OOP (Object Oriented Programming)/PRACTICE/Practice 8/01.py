def main():
    file = open('practice8.txt', 'r')
    red = file.read()
    print(red)
    file.colse()
main()