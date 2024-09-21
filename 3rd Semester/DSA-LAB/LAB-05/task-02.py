from class_node import *


if __name__ == '__main__':
    node = Node(1)
    node = recursive_add_back_node(node, 2)
    node = recursive_add_back_node(node, 3)
    node = recursive_add_back_node(node, 4)
    node = recursive_add_back_node(node, 5)
    node = recursive_add_back_node(node, 6)
    node = recursive_add_back_node(node, 7)
    node = recursive_add_back_node(node, 8)
    node = recursive_add_back_node(node, 9)
    node = recursive_add_back_node(node, 10)
    node = recursive_add_back_node(node, 0)
    print('Before removal:', end=' ')
    recursive_print_linked_nodes(node)
    print('\n')
    
    node = recursive_remove_node(node, 0)
    
    print('After removal:', end=' ')
    recursive_print_linked_nodes(node)
    print('\n')
    print('Reverse:', end=' ')
    reverse_recursive_print_linked_nodes(node)
    
    
    
    print('\n')
    print(f'Recusive count: {recursive_count_linked_nodes(node)}')
    
    