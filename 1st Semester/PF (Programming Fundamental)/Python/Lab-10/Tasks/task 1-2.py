def isNumber(numString):
    index = len(numString) - 1
    while(index >= 0):
        if(ord(numString[index]) < 48 or ord(numString[index]) > 57 ):
            return False
        index -= 1
    return True


print(isNumber('1234567890'))
print(isNumber('123Ab56'))
print(isNumber('aDef881'))
print(isNumber('105opf333'))
print(isNumber('100'))