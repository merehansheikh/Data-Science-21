import copy
# this class is the implementation of 0 based indecing heap.
class MaxHeap:
    def __init__(self, array=None):
        self.heap = []

        if array != None:
            self.heap = array
            for i in range(len(self.heap)):
                self._heapify_up(i)
            
    # Just for the sake of Assignment(this function is also called heapify)
    def _build_heap(self, arr):
        self.heap = arr
        MaxHeap.__init__(arr)
        # self._heapify_up(len(self.heap)-1)

    def insert(self, value):
        # Add new value to the end of the heap
        self.heap.append(value)
        # Heapify up from the last index
        self._heapify_up(len(self.heap) - 1)

    # This pop function is also the implementation of delete max function
    def pop(self):
        if len(self.heap) == 0:
            raise Exception('Heap is empty')
        # Swap the root (max value) with the last value in the heap
        self._swap(0, len(self.heap) - 1)
        # Pop the max value from the heap (which is now at the end)
        max_value = self.heap.pop()
        # Heapify down from the root
        self._heapify_down(0)
        return max_value
    
    def delete_max(self):
        if len(self.heap) == 0:
            raise Exception('Heap is empty')
        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        # While the current index is not the root and its parent is less than it
        while index > 0 and self.heap[(index - 1) // 2] < self.heap[index]:
            # Swap the current index with its parent
            parent_index = (index - 1) // 2
            self._swap(parent_index, index)
            # Set the current index to its parent's index
            index = parent_index

    def _heapify_down(self, index):
        # While the current index has at least one child
        while index * 2 + 1 < len(self.heap):
            left_child_index = index * 2 + 1
            right_child_index = index * 2 + 2
            # Find the index of the maximum child (or left child if only one child)

            max_child_index = left_child_index
            
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[max_child_index]:
                max_child_index = right_child_index
                
            # If the current index is already greater than the maximum child, stop
            if self.heap[index] >= self.heap[max_child_index]:
                break
            # Otherwise, swap the current index with the maximum child
            self._swap(index, max_child_index)
            # Set the current index to the maximum child's index
            index = max_child_index

    def _swap(self, i, j):
        # Swap the values at the given indices
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __len__(self) -> int:
        # Return the number of elements in the heap
        return len(self.heap)

    def is_empty(self):
        # Return True if the heap is empty, False otherwise
        return len(self.heap) == 0

    def peek(self):
        if len(self.heap) == 0:
            raise Exception('Heap is empty')
        # Return the root value (max value)
        return self.heap[0]

    def __str__(self) -> str:
        # Return the string representation of the heap
        return str(self.heap)

    def extract_max(self):
        return self.delete_max()
    
    def find_max(self):
        if len(self.heap) != 0:
            return self.heap[0]
        else:
            raise Exception('Heap is empty')
        
    def increase_key(self, index, delta):
        if not self.is_empty():
            self.heap[index] += delta
            self._swap(index, len(self.heap)-1)
            self._heapify_up(len(self.heap) - 1)
            # self._heapify_up(index) (or)
            
        else:
            raise Exception('Heap is empty')
        
    def decrease_key(self, index, delta):
        if not self.is_empty():
            self.heap[index] -= delta
            self._swap(index, len(self.heap)-1)
            self._heapify_up(len(self.heap) - 1)
            # self._heapify_up(len(index) (or)
            
        else:
            raise Exception('Heap is empty')
        
    def delete_key(self, i):
        self.heap.pop(i)
        self._heapify_up(len(self.heap)-1)
        
    def clear(self):
        self.heap.clear()
        
    def heap_size(self):
        return len(self.heap)
    
    
    def heap_sort(self):
        size  = len(self.heap)
        l = [0]* size
        hehe = -1
        while self.heap:
            # l.append(self.extract_max())
            l[hehe] = self.extract_max()
            hehe -= 1
        # print(l)
        self.heap = copy.deepcopy(l)
        
        
        
    def check_sort(self):
        v =self.size
        for i in range(v):
            temp =self.heap[0]
            self.heap[0] =self.heap[self.size-1]
            self.heap[self.size-1] =temp
            self.size -=1
            self.shiftdown(0)
        self.size =v
