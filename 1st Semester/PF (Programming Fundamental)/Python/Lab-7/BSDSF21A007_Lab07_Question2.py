def isNumber(s):
    i = 0
    count = 0
    while i < len(s):
        if s[i]>= "0" and s[i]<="9":
            count = count + 1
        else:
            pass
        i = i + 1
    if count == len(s):
        return True
    elif count != len(s):
        return False
def main():
    s = "651789"
    num = isNumber(s)
    print(num)
main()
