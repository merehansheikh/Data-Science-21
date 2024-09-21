
import math
def merge(arr, start, mid, end):
    temp = [0] * (end - start +1)
    
    i ,j ,k = start, mid+1, 0
    
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k+=1
            i +=1
        else:
            temp[k] = arr[j]
            k+=1
            j+=1
        
    # for left if left any
    while i <= mid:
        temp[k] = arr[i]
        k +=1
        i +=1
    
    # for right if left any
    while j <= end :
        temp[k] = arr[j]
        k += 1
        j += 1
        
    for i in range(start, end+1):
        arr[i] = temp[i - start]
        

def merge_sort(arr, start, end):
    
    if start < end:
        
        mid = math.floor((start + end) /2)
        
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        
        merge(arr ,start, mid, end)  
        
              
        
if __name__ == '__main__':
    arr= [6,2,1,9,5]
    merge_sort(arr, 0, (len(arr) - 1))
    print(arr)