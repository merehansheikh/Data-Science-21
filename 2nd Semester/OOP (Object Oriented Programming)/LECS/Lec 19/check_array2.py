import random as r
from array import *
array1 = array('i')
print(f'Array: {array1}')
for i in range(10):
    array1.append(r.randint(0,100000))
print(array1)
print(f'Address of Array1: {id(array1)}')
array2 = array1
print(f'Address of Array2: {id(array2)}')
array1.append(r.randint(0,100000))
print(f'Address of Array1: {id(array1)}')
print(f'Address of Array2: {id(array2)}')
print(array2)
