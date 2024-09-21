# from binary_search_tree import *    
from bst_modified import *

if __name__ == '__main__':
    
    
    tree = BinarySearchTree()
    tree.insert(57)
    tree.insert(42)
    tree.insert(62)
    tree.insert(17)
    tree.insert(40)
    tree.insert(88)
    tree.insert(39)
    tree.insert(90)
    tree.insert(99)
    tree.insert(32)
    
    
    
    # print(tree.display())
    # print(tree.search(1))
    
    print('The in order traversel of the tree is: ',end = '')
    tree.traverse_in_order()
    
    # tree.traverse_hehe()
    