def funQuad (a, b, c):
    x1 = ((-b) + ((b**2) - (4*a*c))) / (2*a)
    x2 = ((-b) - ((b**2) - (4*a*c))) / (2*a)
    return (x1, x2)

def main():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    c = int(input("Enter the value of c:"))
    Quadratic = funQuad(a, b, c)
    print(Quadratic)
main()
