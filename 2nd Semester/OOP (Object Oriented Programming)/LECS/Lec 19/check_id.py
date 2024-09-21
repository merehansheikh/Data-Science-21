x = 5
print(f'Address of X: {id(x)}')
x = 7
print(f'Address of X: {id(x)}')
f = 3.2
print(f'Address of F: {id(f)}')
f = 3.23
print(f'Address of F: {id(f)}')
b = True
print(f'Address of B: {id(b)}')
b = False
print(f'Address of B: {id(b)}')

y = x
print(f'Address of Y: {id(y)}')
cf = f
print(f'Address of CF: {id(cf)}')
cb = b
print(f'Address of CB: {id(cb)}')

y = 7
print(f'Address of Y: {id(y)}')
cf = 3.2
print(f'Address of CF: {id(cf)}')
cb = False
print(f'Address of CB: {id(cb)}')
