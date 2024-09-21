# from tree_v2 import *
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
        
        # t.addnode(69, 72)
        
        t.addnode(92, 200)
        t.addnode(60, 200)        
        print('-------------')
        print('The Tree is', end = ' ')
        t.iterative_transversal_by_queue()
        print('-------------')
        print(f'The size of the tree is: {t.size()}')
        print('-------------')
        print(f'The leaves in the tree are: {t.leaves()}')
        print('-------------')
        # print('Updated Tree is: ')
        # t.update(70, 22)
        # t.iterative_transversal_by_queue()
        
        t.cut_paste(50, 60)
        print('-------------')
        # t.level_wise()
        t.Display()
        # print(t.max_depth())
        
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