from class_node import *
    
if __name__ == '__main__':
    node = Node(1)
    addFrontNode(node, 2)
    addFrontNode(node, 3)
    addFrontNode(node, 4)
    recursive_add_front_node(node, 8)
    addBackNode(node, 0)
    # node  = recursive_add_back_node(node, 0)
    # addFrontNode(node, 3)
    # addFrontNode(node, 8)
    # addFrontNode(node, 7)
    # print(sum_linked_nodes(node))
    # recursive_remove_node(node, 2)
    printLinkedNodes(node)
    
    # printLinkedNodes(sortLinkedNodes(node))
