def vowels(s,n):
    count = 0
    i = 0
    while i < n :
        if s[i] == 'a' or s[i] == 'A':
            count = count + 1
        elif s[i] == 'e' or s[i] == 'E':
            count = count + 1
        elif s[i] == 'i' or s[i] == 'I':
            count = count + 1
        elif s[i] == 'o' or s[i] == 'O':
            count = count + 1
        elif s[i] == 'u' or s[i] == 'U':
            count = count + 1
        i = i + 1
    return count
def main():
    string = str(input("Enter a string: "))
    leng = len(string)
    cnt = vowels(string, leng)
    print (cnt)
main()
