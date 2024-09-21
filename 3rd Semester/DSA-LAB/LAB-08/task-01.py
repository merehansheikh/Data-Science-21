class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedListNode:
    
            
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def append(self, data):
        node = Node(data)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
    def remove(self, data):
        node = self.head.next
        while node is not self.tail:
            if node.data == data:
                node.prev.next = node.next
                node.next.prev = node.prev
                break
            node = node.next
        
    def __len__(self):
        node = self.head.next
        count = 0
        while node is not self.tail:
            count += 1
            node = node.next
        return count
    def __iter__(self):
        node = self.head.next
        while node is not self.tail:
            yield node.data
            node = node.next
            
    def print(self):
        node = self.head.next
        while node is not self.tail:
            print(node.data)
            node = node.next

def get_data(n):
    
    my_dict = dict()
    for i in range(n):
        my_dict[input('Name: ')] = input('Lucky Number: ')
    return my_dict
def sort_data(dic):
    k = list(dic.keys())
    new_dict = dict()
    k.sort()
    for i in k:
        new_dict[i] = dic[i]
    print('lol', new_dict)
    return new_dict

        
        
# implementation of the doubly linked list

if __name__ == '__main__':
    
    obj = DoublyLinkedListNode()
    
    dic = sort_data(get_data(int(input('Enter the number of friends:'))))

    for key, value in dic.items():
        obj.append(list((key, value)))
    obj.print()
    print(len(obj))
