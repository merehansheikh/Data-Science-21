from array_stack import *


def infix_to_postfix_conversion(impression):
    """Converts an infix function to a postfix function"""
    stack = ArrayStack()
    postfix = []
    for ele in(impression):
        if ele == '(':
            stack.push(ele)
        elif ele == ')':
            while stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()

        elif ele in '+-*/':
            while not stack.isEmpty() and stack.peek() != '(' and stack.peek() != '+' and stack.peek() != '-':
                postfix.append(stack.pop())
            stack.push(ele)
        else:
            postfix.append(ele)
    while not stack.isEmpty():
        postfix.append(stack.pop())
    return postfix


def main():
    # s = '3+4*5/6'
    s = '2+((2*5)/5)+2'
    print(infix_to_postfix_conversion(s))


main()
