from LinkedStack import *


def ParenthesisCheck(word):
    stack = LinkedStack()
    for i in word:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    for i in word:
        if i == "{":
            stack.push(i)
        elif i == "}":
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    for i in word:
            if i == "[":
                stack.push(i)
            elif i == "]":
                if stack.isEmpty():
                    return False
                else:
                    stack.pop()
    return stack.isEmpty()


if __name__ == '__main__':
    print(ParenthesisCheck("{(()[]{{}})}"))
    print(ParenthesisCheck("{"))