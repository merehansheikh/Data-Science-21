import numpy as np
import random as r

array1 = np.array([r.randint(0,8) for i in range(10)])
print(f'Array: {array1}')
array1 += 1
print(f'Array: {array1}')
array1 *= 2
print(f'Array: {array1}')
