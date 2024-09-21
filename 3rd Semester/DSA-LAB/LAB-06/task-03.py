from LinkedStack import *

def PostFixExpression(word):
    stack = LinkedStack()
    for i in word:
        if i == "+":
            stack.push(stack.pop() + stack.pop())
        elif i == "-":
            stack.push(stack.pop() - stack.pop())
        elif i == "*":
            stack.push(stack.pop() * stack.pop())
        elif i == "/":
            stack.push(stack.pop() / stack.pop())
        else:
            stack.push(int(i))
    return stack.pop()


if __name__ == '__main__':
    print(PostFixExpression('543*+'))