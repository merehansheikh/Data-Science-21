def properCase(s, N):
    i = 0
    r = ""
    while i<N:
        if s[i] == s[0]:
            if ord(s[i])>=ord("a") and ord(s[i]) <= ord("z"):
                r = r + chr(ord(s[i]) - ord("a") + ord("A"))
        elif s[i] == ' ' or s[i] == ".":
            r = r + s[i]
            i = i + 1
            r = r + chr(ord(s[i]) - ord("a") + ord("A"))
        elif s[i] >= "A" and s[i] <="Z":
            r = r + chr(ord(s[i]) + ord("a") - ord("A"))
        else:
            r = r + s[i]
        i = i + 1
    return r
def main():
    s = "soban.anjum"
    lent = len(s)
    proper = properCase(s, lent)
    print(proper)
main()
