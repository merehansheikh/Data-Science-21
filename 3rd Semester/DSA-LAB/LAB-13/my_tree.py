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
                tur = self.addnodeAux(self.root, n, p)
                if tur == None:
                    raise Exception('Chutti Kr Shorya')
    def addnodeAux(self, r, n, p):
        if len(r.children) == 0:
            return 
        chk = None
        for c in r.children:
            if c.data == p:
                c.children.append(self.Node(n))
                return 'Hui Hui'
            chk = self.addnodeAux(c, n, p)
            if chk != None:
                return chk

    def Display(self):
        self.DisplayAux(self.root, 0)
        print()

    def DisplayAux(self, r, level):
        if r != None:
            print("    "*level, r.data, sep="")
            for c in r.children:
                self.DisplayAux(c, level+1)
             
             
             
             
                
    # def iterative_transversal(self):
    #     if self.root == None:
    #         return
    #     stk = [self.root]
    #     while len(stk) > 0:
    #         cur = stk[-1]
    #         del stk[-1]
    #         for c in reversed(cur.children):
    #             stk.append(c)
    #         print(cur.data)
            
    def iterative_transversal_by_queue(self):
        if self.root == None:
            return
        q = [self.root]
        while len(q) > 0:
            cur = q[0]
            del q[0]
            for c in cur.children:
                q.append(c)
            print(cur.data, end = ' ')
        print()
