# linked nodes based code for implementation of TREE basics
class BinTree:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.left_child = None
            self.middle_child = None
            self.right_child = None

    def __init__(self):
        self.root = None

    class PreIterator:
        def __init__(self, node):
            self.stk = [node]

        def __next__(self):
            if len(self.stk) > 0:
                cur = self.stk[-1]
                del self.stk[-1]
                if cur.left_child != None:
                    self.stk.append(cur.left_child)
                if cur.middle_child != None:
                    self.stk.append(cur.middle_child)
                if cur.right_child != None:
                    self.stk.append(cur.right_child)
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
            if self.root.data == p and self.root.left_child == None:
                self.root.left_child = self.Node(n)
                return
            self.addleftchildAux(self.root, n, p)

    def addleftchildAux(self, c, n, p):
        if c != None:
            if c.data == p and c.left_child == None:
                c.left_child = self.Node(n)
                return
            else:  # still a bug here, either of two should be called
                self.addleftchildAux(c.left_child, n, p)
                self.addleftchildAux(c.middle_child, n, p)
                self.addleftchildAux(c.right_child, n, p)

    def addmiddlechild(self, n, p=None):  # middle child lol
        if p == None:
            raise Exception("Parent key required")
        elif n != None and p != None:
            if self.root.data == p and self.root.middle_child == None:
                self.root.middle_child = self.Node(n)
                return
            self.addmiddlechildAux(self.root, n, p)

    def addmiddlechildAux(self, c, n, p):
        if c != None:
            if c.data == p and c.middle_child == None:
                c.middle_child = self.Node(n)
                return
            else:
                self.addmiddlechildAux(c.left_child, n, p)

                self.addmiddlechildAux(c.middle_child, n, p)

                self.addmiddlechildAux(c.right_child, n, p)

    def addrightchild(self, n, p=None):
        if p == None:
            raise Exception("Parent key required")
        elif n != None and p != None:
            if self.root.data == p and self.root.right_child == None:
                self.root.right_child = self.Node(n)
                return
            self.addrightchildAux(self.root, n, p)

    def addrightchildAux(self, c, n, p):
        if c != None:
            if c.data == p and c.right_child == None:
                c.right_child = self.Node(n)
                return
            else:
                self.addrightchildAux(c.left_child, n, p)
                self.addrightchildAux(c.middle_child, n, p)
                self.addrightchildAux(c.right_child, n, p)

    def Display(self):
        self.DisplayAux(self.root, 0)
        print()

    def DisplayAux(self, c, level):
        if c != None:
            print("    "*level, level, ': ',  c.data, sep="")
            self.DisplayAux(c.left_child, level+1)
            self.DisplayAux(c.middle_child, level+1)
            self.DisplayAux(c.right_child, level+1)

    def iterative_traversel_by_queue(self):
        if self.root == None:
            return
        q = [self.root]
        while len(q) > 0:
            cur = q.pop(0)
            # cur = q[0]
            # del q[0]
            print(cur.data, end=" ")
            if cur.left_child != None:
                q.append(cur.left_child)
            if cur.middle_child != None:
                q.append(cur.middle_child)
            if cur.right_child != None:
                q.append(cur.right_child)
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
