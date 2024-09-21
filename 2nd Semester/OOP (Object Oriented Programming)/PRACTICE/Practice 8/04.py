from itertools import count


def main():
    file = open('practice8.txt', 'r')
    r = file.read()
    count = 0
    for i in r:
        count += 1
    print(count)
    file.close()
main()