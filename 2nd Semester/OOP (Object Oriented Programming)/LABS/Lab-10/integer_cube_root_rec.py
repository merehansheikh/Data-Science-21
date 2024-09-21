import random as r
def int_cube_root(x, r=1):
    cube = r * r * r
    if cube == x:  return r
    if cube > x:   return r - 1
    return int_cube_root(x, r+1)

def main():
    for i in range(10):
        x = r.randint(1, 500)
        print (f'Cube root of {x} is {int_cube_root(x)}', end='\t')

main()
