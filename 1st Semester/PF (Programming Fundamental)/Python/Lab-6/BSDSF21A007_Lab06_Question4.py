class matrix():
    a11 = 0
    a12 = 0
    a21 = 0
    a22 = 0
def main():
    x = matrix()
    x.a11 = int(input("Enter the value of a11: "))
    x.a12 = int(input("Enter the value of a11: "))
    x.a21 = int(input("Enter the value of a11: "))
    x.a22 = int(input("Enter the value of a11: "))
    determinant = (x.a11*x.a21) - (x.a12*x.a22)
    print(x.a11, "   ", x.a12)
    print(x.a21, "   ", x.a22)
    print("And The determinant of the the Matrix is: ", determinant)
main()
