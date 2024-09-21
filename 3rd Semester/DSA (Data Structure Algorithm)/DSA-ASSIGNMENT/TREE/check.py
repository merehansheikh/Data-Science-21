class Tree:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.children = []

        def __repr__(self):
            return f"Node({self.data})"

    def __init__(self):
        self.root = None

    class PreIterator:
        def __init__(self, node, tree):
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

    class LevelIterator:
        def __init__(self, node, tree):
            self.q = [node]

        def __next__(self):
            if len(self.q) > 0:
                cur = self.q[0]
                del self.q[0]
                for c in cur.children:
                    self.q.append(c)
                return cur.data
            else:
                raise StopIteration

    def __iter__(self):
        return self.PreIterator(self.root, self)

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

    def display(self):
        self.display_aux(self.root)
        print()

    def display_aux(self, r):
        if r is not None:
            print(r.data)
            for c in r.children:
                self.display_aux(c)

    def size(self):
        return self.size_aux(self.root)

    def size_aux(self, r):
        if r is None:
            return 0
        count = 1
        for c in r.children:
            count += self.size_aux(c)
        return count

    def leaves(self):
        return self.leaves_aux(self.root)

    def leaves_aux(self, r):
        if r is None:
            return 0
        if len(r.children) == 0:
            return 1
        count = 0
        for c in r.children:
            count += self.leaves_aux(c)
        return count

    def update(self, o, n):
        self.update_aux(self.root, o, n)

    def update_aux(self, r, o, n):
        if r is not None:
            if r.data == o:
                r.data = n
            for c in r.children:
                self.update_aux(c, o, n)

    def level_wise(self):
        q = [self.root]
        while len(q) > 0:
            cur = q.pop(0)
            print(cur.data)
            for c in cur.children:
                q.append(c)

    def depth(self, n):
        return self.depth_aux(self.root, n, 0)

    def depth_aux(self, r, n, level):
        if r is None:
            return None
        if r.data == n:
            return level
        for c in r.children:
            d = self.depth_aux(c, n, level+1)
            if d is not None:
                pass

    def depth(self, n):
        def depthAux(r, n, curDepth):
            if r.data == n:
                return curDepth
            for c in r.children:
                d = depthAux(c, n, curDepth + 1)
                if d != -1:
                    return d
            return -1

        return depthAux(self.root, n, 0)
