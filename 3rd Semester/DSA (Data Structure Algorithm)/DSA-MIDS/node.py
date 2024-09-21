# creating a class of nodes
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next 
        
#  add a node to the back of the linked list
def addBackNode(lnkNodes, val):
    tmp = Node(val)
    tmp.next = lnkNodes
    lnkNodes = tmp
    return lnkNodes

# add a node to the front of the linked list
def addFrontNode(lnkNodes, val):
    tmp = Node(val)
    cn = lnkNodes
    while cn.next != None:
        cn = cn.next
    cn.next = tmp
    return lnkNodes

# printing the linked list
def printLinkedNodes(lnkNodes):
    cn = lnkNodes
    # while cn is not None:   (Is true also)
    while cn:
        print(cn.data, end=" ")
        cn = cn.next
    print()

# remove a node from the linked list
def removeNode(lnkNodes, val):
    cn = lnkNodes
    if cn.data == val:
        lnkNodes = cn.next
        del cn
        return lnkNodes
    
    while cn.next != None:
        if cn.next.data == val:
            tmp = cn.next
            cn.next = tmp.next
            del tmp
        cn = cn.next
    return lnkNodes
        
# return the sum of the linked list
def sum_linked_nodes(lnkNodes):
    cn = lnkNodes
    sum = 0
    while cn != None:
        sum += cn.data
        cn = cn.next
    return sum

# return the count of the linked list
def count_linked_nodes(lnkNodes):
    cn = lnkNodes
    count = 0
    while cn != None:
        count += 1
        cn = cn.next
    return count



#       <-------------- recursive functions -------------->


def recursive_add_front_node(lnkNodes, val):
    if lnkNodes == None:
        return Node(val)
    else:
        lnkNodes.next = recursive_add_front_node(lnkNodes.next, val)
        return lnkNodes
    
def recursive_add_back_node(lnkNodes, val):
    if lnkNodes == None:
        return Node(val)
    else:
        tmp = Node(val)
        tmp.next = lnkNodes
        return tmp 

def recursive_print_linked_nodes(lnkNodes):
    if lnkNodes == None:
        return
    else:
        print(lnkNodes.data, end=" ")
        recursive_print_linked_nodes(lnkNodes.next)
    
def recursive_remove_node(lnkNodes, val):
    if lnkNodes == None:
        return None
    else:
        if lnkNodes.data == val:
            return lnkNodes.next
        else:
            lnkNodes.next = recursive_remove_node(lnkNodes.next, val)
            return lnkNodes

def reverse_recursive_print_linked_nodes(lnkNodes):
    if lnkNodes == None:
        return
    else:
        reverse_recursive_print_linked_nodes(lnkNodes.next)
        print(lnkNodes.data, end=" ")

def recursive_count_linked_nodes(lnkNodes):
    if lnkNodes == None:
        return 0
    else:
        return 1 + recursive_count_linked_nodes(lnkNodes.next)
    
    
    
# <------------------ sorting nodes ------------------>

def sortLinkedNodes(lnkNodes):
    cn = lnkNodes
    while cn:
        cn2 = cn.next
        while cn2:
            if cn.data > cn2.data:
                tmp = cn.data
                cn.data = cn2.data
                cn2.data = tmp
            cn2 = cn2.next
        cn = cn.next
    return lnkNodes