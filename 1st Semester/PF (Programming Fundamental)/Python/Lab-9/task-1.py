def printTriangle(a,b):
    i = ord(a)
    while i <=ord(b):
        q = ord(a)
        while q<=i:
            print(chr(q),end="")
            q = q + 1

        i = i + 1
        print()
def main():
    chr1 = str(input())
    chr2 = str(input())
    printTriangle(chr1,chr2)
main()
