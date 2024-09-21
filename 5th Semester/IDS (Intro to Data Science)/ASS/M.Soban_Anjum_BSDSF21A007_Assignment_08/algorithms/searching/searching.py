def linear_search(arr:list, target:int) -> int:
    """
    Perform Linear Search on a given list.

    Parameters:
    arr (list): The list to be searched.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr:list, target:int) -> int:
    """
    Perform Binary Search on a given sorted list.

    Parameters:
    arr (list): The sorted list to be searched.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def interpolation_search(arr:list, target:int) -> int:
    """
    Perform Interpolation Search on a given sorted list.

    Parameters:
    arr (list): The sorted list to be searched.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        mid = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def exponential_search(arr:list, target:int) -> int:
    """
    Perform Exponential Search on a given sorted list.

    Parameters:
    arr (list): The sorted list to be searched.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, else -1.
    """
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return binary_search(arr[:min(i, n)], target)

def jump_search(arr:list, target:int) -> int:
    """
    Perform Jump Search on a given sorted list.

    Parameters:
    arr (list): The sorted list to be searched.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, else -1.
    """
    
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev
    else:
        return -1


if __name__ == "__main__":
    testing_data = [1, 2, 2, 3, 3, 5, 7, 9, 69, 420]

    # Linear Search
    found = linear_search(testing_data, 69)
    print("Linear Search:", found)

    # Binary Search
    found = binary_search(testing_data, 699)
    print("Binary Search:", found)

    # Interpolation Search
    found = interpolation_search(testing_data, 966)
    print("Interpolation Search:", found)

    # Exponential Search
    found = exponential_search(testing_data, 420)
    print("Exponential Search:", found)

    # Jump Search
    found = jump_search(testing_data, 204)
    print("Jump Search:", found)
