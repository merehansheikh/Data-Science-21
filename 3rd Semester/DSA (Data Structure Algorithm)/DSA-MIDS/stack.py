class Node:
    def __init__(self,val):
        self.data =val
        self.link =None
class LinkedStacks:
    def __init__(self):
        self.head =None
        self.size =0
    
    def push(self,val):
        tmp =Node(val)
        if self.head==None:
            self.head =tmp
            
        else:
            tmp.link =self.head
            self.head =tmp
        self.size +=1
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from empty array")
        else:
            self.size -=1
            tmp =self.head
            self.head =self.head.link
            return tmp.data
    def peek(self):
        if self.is_empty():
            raise Exception("Empty arr")
        return self.head.data

    def is_empty(self):
        return self.head==None
    def get_size(self):
        return self.size
def palindrome(s):
    st =""
    l =LinkedStacks()
    for i in range(len(s)):
        l.push(s[i])
    for j in range(len(s)):
        st +=l.pop()

    return st==s
def parenthesis(s):
    l =LinkedStacks()
    for i in range(len(s)):
        if s[i] in ["(","[","{"]:
            l.push(s[i])
        else:
            if l.is_empty()==True:
                return False
            if s[i] == "}" and l.peek() == "{":
                l.pop()
            elif s[i] ==  "]" and l.peek() == "[":
                l.pop()
            elif s[i] == ")" and l.peek() == "(":
                l.pop()
            
    return l.is_empty()
def postfix(s):
        l =LinkedStacks()
        for i in range(len(s)):
            if s[i]=="+":
                first = l.pop()
                second = l.pop()
                sum = first+ second
                l.push(sum)


            elif s[i]=="-":
                first = l.pop()
                second = l.pop()
                sub = second - first
                l.push(sub)

            elif s[i]=="*":
                first = l.pop()
                second = l.pop()
                mul = first * second
                l.push(mul)
                
            elif s[i]=="/":
                first = l.pop()
                second = l.pop()
                div = second / first
                l.push(div)
            else:
                l.push(int(s[i]))

        return l.head.data
def main():
    # l =LinkedStacks()
   
    # print(l.is_empty())
    # l.push(10)
    # l.push(11)
    # print(l.is_empty())
    # print(l.peek())
    # l.pop()
    # print(l.peek())
    # print(l.get_size())
    # print(palindrome("civic"))
    # print()
    print(parenthesis("([{([]())}])"))
    print(postfix("359+*"))



main()

