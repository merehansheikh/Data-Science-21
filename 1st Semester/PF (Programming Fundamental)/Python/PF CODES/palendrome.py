def palindrome(s):
    i = len(s)
    rev = ''
    while i >0:
        rev = rev + s[i-1]
        i = i - 1
    print(rev)
    if rev == s:
        return True
    else:
        return False
print(palindrome('1234321'))
