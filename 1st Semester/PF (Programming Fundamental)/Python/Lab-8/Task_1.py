def isPerfectSquare(n):
    i = 1
    while i < n:
        if i * i == n:
            return "Perfect square"
        else:
            i += 1
def main():
    n = int(input())
    isPerfectSquare(n)
main()