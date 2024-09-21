import random as r
from array import *
array1 = array('i', [23, 65, 78])
print(f'Array: {array1}')
print(f'Reference/ Handler address: {id(array1)}')
print(f'Current Object address: {str(array1.buffer_info()[0])}')
print(f'Count of elements: {str(array1.buffer_info())}')
print(f'Count of elements: {len(array1)}')
for i in range(1000):
    array1.append(r.randint(0,100000))
print(f'Reference/ Handler address: {id(array1)}')
print(f'Current Object address: {str(array1.buffer_info()[0])}')
print(f'Count of elements: {len(array1)}')
