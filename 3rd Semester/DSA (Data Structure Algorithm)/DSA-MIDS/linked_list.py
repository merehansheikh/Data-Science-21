class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
            
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = self.Node(value)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value)
            self.tail = self.tail.next
    
        
    def remove(self, value):
        if self.head is None:
            raise Exception("List is empty")
        elif self.head.data == value:
            self.head = self.head.next
        else:
            cn = self.head
            while cn.next is not None:
                if cn.next.data == value:
                    cn.next = cn.next.next
                    return
                cn = cn.next
            raise Exception("Value not found")

    def __str__(self):
        cn = self.head
        result = ""
        while cn:
            result += str(cn.data) + " "
            cn = cn.next
        return result
    
    def print(self):
        cn = self.head
        while cn:
            print(cn.data, end=" ")
            cn = cn.next
        print()
    
    def pop(self):
        if self.head is None:
            raise Exception("List is empty")
        else:
            tmp = self.head
            self.head = self.head.next
            return tmp.data
        
    def add_after(self, value, new_value):
        cn = self.head
        while cn:
            if cn.data == value:
                cn.next = self.Node(new_value, cn.next)
                return
            cn = cn.next
        raise Exception("Value not found")
    
    def add_before(self, value, new_value):
        if self.head.data == value:
            self.head = self.Node(new_value, self.head)
        else:
            cn = self.head
            while cn.next:
                if cn.next.data == value:
                    cn.next = self.Node(new_value, cn.next)
                    return
                cn = cn.next
            raise Exception("Value not found")
