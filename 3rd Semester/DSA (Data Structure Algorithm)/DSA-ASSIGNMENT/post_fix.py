from array_stack import *

def post_fix(expr):
    stack = ArrayStack()
    for i in expr:
        if i.isdigit():
            stack.push(i)
        else:
            if i == "+":
                stack.push(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                stack.push(int(stack.pop()) - int(stack.pop()))
            elif i == "*":
                stack.push(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                stack.push(int(stack.pop()) / int(stack.pop()))
    return stack.pop()