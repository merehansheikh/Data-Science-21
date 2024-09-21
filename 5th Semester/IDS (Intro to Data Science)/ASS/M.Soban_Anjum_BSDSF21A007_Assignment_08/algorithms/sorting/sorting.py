def bubble_sort(arr:list) -> list:
    """
    Perform Bubble Sort on a given list.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr:list) -> list:
    """
    Perform Selection Sort on a given list.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr:list) -> list:
    """
    Perform Insertion Sort on a given list.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr:list) -> list:
    """
    Perform Merge Sort on a given list.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr:list) -> list:
    """
    Perform Quick Sort on a given list.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    
    testing_data = [7,3,2,1,9,5,3,2,69,420]

    # Bubble Sort 
    b_sorted_data = bubble_sort(testing_data.copy())
    print("Bubble Sort:", b_sorted_data)

    # Selection Sort 
    s_sorted_data = selection_sort(testing_data.copy())
    print("Selection Sort:", s_sorted_data)

    # Insertion Sort 
    i_sorted_data = insertion_sort(testing_data.copy())
    print("Insertion Sort:", i_sorted_data)

    # Merge Sort 
    m_sorted_data = merge_sort(testing_data.copy())
    print("Merge Sort:", m_sorted_data)

    # Quick Sort
    q_sorted_data = quick_sort(testing_data.copy())
    print("Quick Sort:", q_sorted_data)
