# linked nodes based code for implementation of TREE basics
class BinTree:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    class PreIterator:
        def __init__(self, node):
            self.stk = [node]

        def __next__(self):
            if len(self.stk) > 0:
                cur = self.stk[-1]
                del self.stk[-1]
                if cur.left != None:
                    self.stk.append(cur.left)
                if cur.right != None:
                    self.stk.append(cur.right)
                return cur.data
            else:
                raise StopIteration

    def __iter__(self):
        return self.PreIterator(self.root)

    def addroot(self, n):
        if self.root == None:
            self.root = self.Node(n)
        else:
            raise Exception("Root aleady exist")

    def addleftchild(self, n, p=None):
        if p == None:
            raise Exception("Parent key required")
        elif n != None and p != None:
            if self.root.data == p and self.root.left == None:
                self.root.left = self.Node(n)
                return
            self.addleftchildAux(self.root, n, p)

    def addleftchildAux(self, c, n, p):
        if c != None:
            if c.data == p and c.left == None:
                c.left = self.Node(n)
                return
            else:  # still a bug here, either of two should be called
                self.addleftchildAux(c.left, n, p)
                self.addleftchildAux(c.right, n, p)

    def addrightchild(self, n, p=None):
        if p == None:
            raise Exception("Parent key required")
        elif n != None and p != None:
            if self.root.data == p and self.root.right == None:
                self.root.right = self.Node(n)
                return
            self.addrightchildAux(self.root, n, p)

    def addrightchildAux(self, c, n, p):
        if c != None:
            if c.data == p and c.right == None:
                c.right = self.Node(n)
                return
            else:  # still a bug here, either of two should be called
                self.addrightchildAux(c.left, n, p)
                self.addrightchildAux(c.right, n, p)

    def Display(self):
        self.DisplayAux(self.root, 0)
        print()

    def DisplayAux(self, c, level):
        if c != None:
            print("    "*level, c.data, sep="")
            self.DisplayAux(c.left, level+1)
            self.DisplayAux(c.right, level+1)
            
    def iterative_traversel_by_queue(self):
        if self.root == None:
            return
        q = [self.root]
        while len(q) > 0:
            cur = q[0]
            del q[0]
            print(cur.data, end=" ")
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)
        print()


# def main():
#     # Create a new BinTree
#     t = BinTree()
#     # add the root element to the BinTree
#     t.addroot(10)
#     # add the element as child node to an existing node of BinTree
#     t.addleftchild(30, 10)
#     t.addrightchild(70, 10)
#     t.addleftchild(90, 30)
#     t.addrightchild(60, 30)
#     t.addleftchild(50, 90)
#     t.addleftchild(40, 70)
#     t.addrightchild(20, 70)

#     # Display BinTree data
#     print("Display BinTree data")
#     t.Display()

#     print()

#     print("OUTPUT of 'for d in t:'")
#     for d in t:
#         print(d)
#     print()


# main()
