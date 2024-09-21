class rational:
    p = 0
    q = 0
def main():
    r = rational
    r.p = int(input("Enter the value of Numerator: "))
    r.q = int(input("Enter the value of Denominator: "))
    if r.q == 0:
       raise Exception('Denominatorshould not be zero')
    else :
        print("The p/q form will be: ", r.p, "/", r.q)
main()
