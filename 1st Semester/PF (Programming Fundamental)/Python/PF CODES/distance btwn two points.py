def funDis(x1, x2, y1, y2):
    dist = (((x2 - x1)**2) + ((y2 - y1)**2)) ** 0.5
    return dist

def main():

    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))
    distance = funDis(x1, x2, y1, y2)
    print("Distance between two points is =", distance)
main()

