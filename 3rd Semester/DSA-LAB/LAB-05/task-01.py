from class_node import *
            
if __name__ == '__main__':
    node = Node(1)
    node = addFrontNode(node, 2)
    node = addFrontNode(node, 3)
    node  = addBackNode(node, 0)
    
    node = recursive_add_back_node(node, 2)
    printLinkedNodes(node)
    # # removing node
    # node = removeNode(node, 0)
    # printLinkedNodes(node)
    
    # print(f'The sum of linked nodes is {sum_linked_nodes(node)}')
    
    # print(f'The count of linked nodes is {count_linked_nodes(node)}') 
    