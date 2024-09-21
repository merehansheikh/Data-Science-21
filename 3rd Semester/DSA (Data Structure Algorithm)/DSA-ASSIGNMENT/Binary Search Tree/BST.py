class BST:
    class Node:
        def __init__(self, data):
            self.data =data
            self.right =None
            self.left =None


    def __init__(self):
        self.root =None

    def addnode(self, val):
        if self.root==None:
            self.root = self.Node(val)
        else:
            self.addnodeaux(self.root, val)

    def addnodeaux(self, r, val):

        if val>r.data:
            if r.right==None:
                r.right =self.Node(val)
                return
            self.addnodeaux(r.right, val)
        else:
            if r.left==None:
                r.left =self.Node(val)
                return
            self.addnodeaux(r.left, val)
            
    def search(self, val):
        return self.searchaux(self.root, val)
    
    def searchaux(self, r, val):
        if r==None:
            return False
        if val>r.data:
            return self.searchaux(r.right, val)
        elif val<r.data:
            return self.searchaux(r.left, val)
        else:
            return True
        
    def traverse(self):
        return self.traverseaux(self.root)
    
    def traverseaux(self, r):
        if r==None:
            return
        self.traverseaux(r.left)
        print(r.data)
        self.traverseaux(r.right)
        
def main():
    b =BST()
    b.addnode(30)
    b.addnode(40)
    b.addnode(10)
    b.addnode(35)
    b.addnode(60)
    b.addnode(90)
    b.addnode(0)
    b.addnode(800)
    b.traverse()
    print(b.search(350))



main()