def noTab(s):
    i  = 0
    r = ""
    while i < (len(s)):
        if s[i]== "\t" :
            r = r + "   "
        else:
            r = r + s[i]
        i = i +1
    return r
def main():
    a = noTab('Muhammad\tSoban\tAnjum')
    print(a)
main()
