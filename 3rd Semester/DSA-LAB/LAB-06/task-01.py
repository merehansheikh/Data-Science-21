from LinkedStack import *

def PalindromeCheck(word):
    stack = LinkedStack()
    for i in word:
        stack.push(i)
    for i in word:
        if i != stack.pop():
            return False
    return True

if __name__ == "__main__":
    print(PalindromeCheck("abba"))
    print(PalindromeCheck("abbabbababbabba"))