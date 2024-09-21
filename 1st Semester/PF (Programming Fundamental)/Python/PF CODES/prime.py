def prime():
    i = 1
    prm = 2
    while i <= 20:
        temp = 2
        while temp < prm:
            if prm % temp == 0:
                break
            temp = temp + 1
        if temp == prm:
            print(prm)
            i = i + 1
        prm = prm + 1


def main():
    print("1st 20 prime numbers are: ")
    prime()

main()

