def toLower(c):
    lower = ''
    i = 0
    strLen = len(c)
    while(i < strLen):
        if(ord(c[i]) >= 65  and ord(c[i]) <= 92):
            lower += chr(ord(c[i]) + 32)
        else:
            lower += c[i]
        i += 1
    return lower

def countVowels(string):
    string = toLower(string)
    count = 0
    index = len(string) - 1 
    while index >= 0:
        if(string[index] == 'a' or string[index] == 'e' or string[index] == 'i' or string[index] == 'o' or string[index] == 'u'):
            count += 1
        index -= 1
    return count
str = toLower("Practice Programming Daily")
print(str)
countofVowels = countVowels('Practice Programming Daily')
print(countofVowels)
    