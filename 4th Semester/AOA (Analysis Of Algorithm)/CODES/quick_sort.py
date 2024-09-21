
def Swap(arr, i ,j):
    arr[i] , arr[j] = arr[j], arr[i]

def partition(arr, left, right):
    x = arr[left]
    i = left
    j = left+1
    
    while j < len(arr):
        
        if arr[j] < x:
            i += 1
            Swap(arr, i , j)
        j += 1
    
    Swap(arr, left, i)
    return i


def quick_sort(arr, left, right):
    
    if left < right:
        q = partition(arr, left, right)
        
        quick_sort(arr, left, q)
        quick_sort(arr, q+1, right)
        

if __name__ == "__main__":
    arr = [-1, 1,2,3,100,4,1,4, 69, -420]
    
    quick_sort(arr, 0, len(arr)-1)
    
    
