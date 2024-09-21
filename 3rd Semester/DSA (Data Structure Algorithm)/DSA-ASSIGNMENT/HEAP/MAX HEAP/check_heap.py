from my_heap_max import *


if __name__ == "__main__":
    
# if we give an array to the class
    arr = [1,2,3,4,5,6,7]
    heap_1 = MaxHeap(arr)
    print('The heap implementation when an array is given:', end=' ')
    print(heap_1)
    
    print('---------------------------------\n')
    
    # if we give values to the heap one by one
    
    heap1 = MaxHeap()
    heap1.insert(1)
    heap1.insert(2)
    heap1.insert(3)
    heap1.insert(4)
    heap1.insert(5)
    heap1.insert(6)
    heap1.insert(7)
    heap1.insert(8)
    heap1.insert(9)
    heap1.insert(10)
    heap1.insert(11)
    print('The implementation of the heap when an we give values one by one:', end= ' ')
    print(heap1)
    print('---------------------------------\n')
    
    
    heap1.pop()
    print('The heap after poping max value that is 9:',heap1)
    
    heap1.delete_max()
    print('The heap after poping max value that is 8 :',heap1)
    
    print('Checking whether the heap is empty or not: ', heap1.is_empty())
    
    
    print('The max value now in the heap is', heap1.find_max())
    
    heap1.increase_key(2, 9)
    
    print('The heap after the increment of 9', heap1)
    
    heap1.decrease_key(2, 9)
    
    print('The heap after the decrement of 9', heap1)
    
    
    print('The size of the heap is: ', heap1.heap_size())
    
    heap1.delete_key(3)
    print('Heap after the deletion of 3rd index: ',heap1)
    
    # heap1.clear()
    # print('The heap after the clearance: ', heap1)
    
    
    print('\n\n-------------------------')
    
    # nums =    [80, 65, 70, 30, 40, 100, 50]
    
    
    # heap2 = MaxHeap(nums)
    # print(heap2)
    # print(nums)
    
    # # heap2.increase_key(5, 65)

    
    # # heapq._heapify_max(nums)
    # # print(nums)
    
    # # print(heap2)
    
    heap1.heap_sort()
    print(heap1)