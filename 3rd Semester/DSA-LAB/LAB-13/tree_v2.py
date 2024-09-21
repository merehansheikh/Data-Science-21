# linked nodes based code for implementation of TREE basics
class Tree:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.children = []

    def __init__(self):
        self.root = None

    class PreIterator:
        def __init__(self, node):
            self.stk = [node]

        def __next__(self):
            if len(self.stk) > 0:
                cur = self.stk[-1]
                del self.stk[-1]
                for c in reversed(cur.children):
                    self.stk.append(c)
                return cur.data
            else:
                raise StopIteration

    def __iter__(self):
        return self.PreIterator(self.root)

    def addnode(self, n, p=None):
        if p == None and self.root == None:
            self.root = self.Node(n)
        elif p == None:
            raise Exception("Root aleady exist")
        elif n != None and p != None:
            if self.root.data == p:
                self.root.children.append(self.Node(n))
            else:
                self.addnodeAux(self.root, n, p)

    def addnodeAux(self, r, n, p):
        for c in r.children:
            if c.data == p:
                c.children.append(self.Node(n))
                return
            self.addnodeAux(c, n, p)

    def Display(self):
        self.DisplayAux(self.root, 0)
        print()

    def DisplayAux(self, r, level):
        if r != None:
            print("    "*level, r.data, sep="")
            for c in r.children:
                self.DisplayAux(c, level+1)
 


# def main():
#     # Create a new tree
#     t = Tree()
#     # add the root element to the tree
#     t.addnode(10)
#     # add the element as child node to an existing node of tree
#     t.addnode(30, 10)
#     t.addnode(200, 10)
#     t.addnode(70, 10)
#     t.addnode(2, 30)
#     t.addnode(50, 30)
#     t.addnode(92, 200)
#     t.addnode(60, 200)
#     t.addnode(12, 70)
#     t.addnode(2000, 60)
#     t.addnode(7000, 60)
#     t.addnode(55, 60)

#     # Display tree data
#     print("Display tree data")
#     t.Display()

#     print()

#     print("OUTPUT of 'for d in t:'")
#     for d in t:
#         print(d)
#     print()


# main()
