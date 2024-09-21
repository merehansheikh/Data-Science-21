def counting_sort(arr):
    # Step 1
    max_element = max(arr)

    # Step 2
    count = [0] * (max_element + 1)

    # Step 3
    for i in arr:
        count[i] += 1

    # Step 4
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Step 5
    result = [0] * len(arr)

    # Step 6
    for i in range(len(arr)-1, -1, -1):
        result[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    # Step 7
    return result



def find_max(arr):
    return max(arr)


def counting_sort(arr):
    max_ = find_max(arr)
    
    count_arr = [0 for i in range(max_+1)]
    
    for ele in arr:
        count_arr[ele] += 1
        
    for i in range(1, len(max_+1)):
        
        count_arr[i] = count_arr[i-1] + count_arr[i]
        
    
    
    
    pass


if __name__ == "__main__":
    arr = [2,3,4,1,6,9,5]
    pass
