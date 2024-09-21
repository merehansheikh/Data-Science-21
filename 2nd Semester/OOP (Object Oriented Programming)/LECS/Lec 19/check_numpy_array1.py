import numpy as np
import random as r

array1 = np.array([r.randint(0,8) for i in range(10)])
print(f'Address of Array Object: {array1.ctypes.data}')
print(f'Address of Array: {id(array1)}')
array1 *= 100000000
print(array1)
print(f'Address of Array: {id(array1)}')
print(f'Address of Array Object: {array1.ctypes.data}')
array1 = np.append(array1,[3,8])
print(array1)
print(f'Address of Array: {id(array1)}')
print(f'Address of Array Object: {array1.ctypes.data}')
