# from tree_v2 import *
from bintree_v1 import *
from my_tree import *

def main_tree():
    if __name__ == '__main__':
        # Create a new tree
        t = Tree()
        # add the root element to the tree
        t.addnode(10)
        # add the element as child node to an existing node of tree
        t.addnode(30, 10)
        t.addnode(200, 10)
        t.addnode(70, 10)
        t.addnode(2, 30)
        t.addnode(50, 30)
        
        t.addnode(69, 72)
        
        t.addnode(92, 200)
        t.addnode(60, 200)
        t.addnode(12, 70)
        t.addnode(2000, 60)
        t.addnode(7000, 60)
        t.addnode(55, 60)
        
        
        print('The Tree is')
        t.iterative_transversal_by_queue()
        # t.Display()
main_tree()

# def main_bintree():
#     if __name__ == '__main__':
#         # Create a new BinTree
#         t = BinTree()
#         # add the root element to the BinTree
#         t.addroot(10)
#         # add the element as child node to an existing node of BinTree
#         t.addleftchild(30, 10)
#         t.addrightchild(70, 10)
#         t.addleftchild(90, 30)
#         t.addrightchild(60, 30)
#         t.addleftchild(50, 90)
#         t.addleftchild(40, 70)
#         t.addrightchild(20, 70)

#         # Display BinTree data
#         print("Display BinTree data")
#         t.iterative_traversel_by_queue()
# main_bintree()