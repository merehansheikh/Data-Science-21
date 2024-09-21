def toUpper(s):
    c = ''
    if(ord(s) >= 97 and ord(s) <= 122):
        c += chr(ord(s) - 32)
    else:
        c += s
    return c

def toLower(s):
    c = ''
    if(ord(s) >= 65 and ord(s) <= 92):
        c += chr(ord(s) + 32)
    else:
        c += s
    return c
    
def properCase(s):
    strLen = len(s)
    i = 1
    properStr = ''
    properStr += toUpper(s[0])
    while (i < strLen):
        if(s[i-1] == '.' or s[i-1] == ' '):
            properStr += toUpper(s[i])
        else:
            properStr += toLower(s[i])
        i += 1
    return properStr

string = 'proGramming is FrustRaTIng at SOmeTimes. you mUst Keep GoinG and ThInGS wilL EveNtuAll bEComEs CleaR TO You'
print(properCase(string))