from my_bintree_v1 import *


if __name__ == '__main__':
    
    # Create a new BinTree
    t = BinTree()
    # add the root element to the BinTree
    t.addroot(10)
    # add the element as child node to an existing node of BinTree
    t.addleftchild(30, 10)
    t.addrightchild(70, 10)
    
    t.addleftchild(90, 30)
    t.addrightchild(60, 30)
    
    t.addleftchild(50, 90)
    t.addleftchild(40, 70)
    
    t.addrightchild(20, 70)
    

    # Display BinTree data
    print("Display BinTree data")
    t.Display()
    t.iterative_traversel_by_queue()
    print()
