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
        return self.update_aux(self.root, o ,n)
    
    def update_aux(self, r, o,n):
        if r is not None:
            if r.data == o:
                r.data = n
            for c in r.children:
                self.update_aux(c, o, n)
             
             
    def max_depth(self):
        if self.root is None:
            return 0
        max_depth = 0
        queue = [(self.root, 1)]
        while queue:
            r, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            for child in r.children:
                queue.append((child, depth + 1))
        return max_depth   
             
    
    def level_wise(self):
        q = [self.root]
        while len(q) > 0:
            cur = q.pop()
            print(cur.data)
            for c in cur.children:
                q.append(c)                
            
    def iterative_transversal_by_stack(self):
        if self.root == None:
            return
        stk = [self.root]
        while len(stk) > 0:
            cur = stk[-1]
            del stk[-1]
            for c in reversed(cur.children):
                stk.append(c)
            print(cur.data)
            
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
        
        
    # def cut_paste(self, o, n):
    #     if self.root is None:
    #         return None
    #     if self.root.data == o:
    #         node = self.root
    #         self.root = None
    #         self.addnode(node.data, n)
    #         for child in node.children:
    #             self.addnode(child.data, node.data)
    #         return
    #     # _ , node = self.find_node(o, self.root, None)
    #     parent, node = self.find_node(o, self.root, None)
    #     if node is None:
    #         return None
    #     self.remove_subtree(node)
    #     self.addnode(node.data, n)
    #     for child in node.children:
    #         self.addnode(child.data, node.data)

    # def find_node(self, o, node, parent):
    #     if node is None:
    #         return None, None
    #     if node.data == o:
    #         return parent, node
    #     for child in node.children:
    #         parent, node = self.find_node(o, child, node)
    #         if node is not None:
    #             return parent, node
    #     return None, None

    # def remove_subtree(self, node):
    #     parent, _ = self.find_node(node.data, self.root, None)
    #     if parent is None:
    #         self.root = None
    #     else:
    #         parent.children = [child for child in parent.children if child.data != node.data]
    #     node.children = []



    def cut_paste(self, o, n):
        cut =self.cut(self.root,o)
        if cut !=None:
            self.paste(self.root,cut,n)
        else:
            raise Exception("Node dont exit")
        
    def cut(self,r, o):
        val = None
        for i in range(len(r.children)):
            if r.children[i].data==o:
                val = r.children[i]
                r.children.remove(r.children[i])
                return val
   
            z = self.cut(r.children[i], o)
            if z != None:
                val = z               
        return val
    
    def paste(self, r, cut, n):
        for c in r.children:
            if c.data == n:
                c.children.append(cut)
                return
            self.paste(c ,cut, n)
            
    def removenode(self,n):
        if self.root.data==n:
            self.root =None
        else:

            v =self.removenodeAux(self.root,n)
            print(v)
            if v!="-":
                raise Exception("Not found")
        
    def removenodeAux(self, r, n):
        if len(r.children)==0:
            return
        v =None
        for c in r.children:
            if c.data==n:
                r.children.remove(c)
                
                return "-"
            v =self.removenodeAux(c, n)
            if v=="-":
                return v

    # def depth(self, n):
    #     def depthAux(r, n, curDepth):
    #         if r.data == n:
    #             return curDepth
    #         for c in r.children:
    #             d = depthAux(c, n, curDepth + 1)
    #             if d != -1:
    #                 return d
    #         return -1

    #     return depthAux(self.root, n, 0)