def bubble(a,n):
    i = 0
    size = n - 1
    while size > i:
        if a[size] < a[size - 1]:
            temp = a[size]
            a[size] = a[size -1]
            a[size-1] = temp
        size = size - 1
    return a

def printArray(a):
    print(a)
def main():
    size = 5
    arr = [0] * size
    i = 0
    while i < size:
        arr[i] = int(input())
        i = i + 1
    print("The random order array is")
    printArray(arr)
    for i in range(size):
        q = bubble(arr, size)
    printArray(q)

main()
# Write your code here :-)
