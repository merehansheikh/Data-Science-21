x = [2,3,4]
print(f'Address of X: {id(x)}')
x.append(6)
for i in range(10000000):
    x.append(1)
print(f'Address of X: {id(x)}')
print(f'Size of X: {len(x)}')

