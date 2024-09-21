
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0  # Initialize height to 0 for each node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
            
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))  # Update node height
        return node

    def _get_height(self, node):
        if not node:
            return -1
        return node.height

    def traverse_in_order(self):
        self.traverse_in_order_aux(self.root)
        
    def traverse_in_order_aux(self, root):
        if root :
            self.traverse_in_order_aux(root.left)
            print(root.val, root.height)
            self.traverse_in_order_aux(root.right)
            
    