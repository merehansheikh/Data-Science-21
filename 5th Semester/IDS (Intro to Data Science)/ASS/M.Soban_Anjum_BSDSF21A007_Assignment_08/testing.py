import time
import random
from algorithms.sorting.sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from algorithms.searching.searching import linear_search, binary_search, interpolation_search, exponential_search, jump_search

# Define functions for generating random arrays
def generate_random_array(size:int) -> list:
    """
    Generate a random array of integers.

    Parameters:
    - size (int): The size of the array to generate.

    Returns:
    - list: A random array of integers.
    """
    return [random.randint(1, 1000) for _ in range(size)]

def generate_sorted_array(size:int) -> list:
    
    """
    Generate a sorted array of integers.

    Parameters:
    - size (int): The size of the array to generate.

    Returns:
    - list: A sorted array of integers.
    """
    
    return list(range(1, size + 1))

# Sorting algorithms comparison
def compare_sorting_algorithms() -> None:
    """
    Compare the performance of different sorting algorithms on arrays of varying sizes.
    """
    sorting_algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort
    }

    array_sizes = [1000, 5000, 10000]

    for algorithm_name, algorithm_func in sorting_algorithms.items():
        print(f"Comparing {algorithm_name}:")

        for size in array_sizes:
            array = generate_random_array(size)

            start_time = time.time()
            sorted_array = algorithm_func(array)
            end_time = time.time()

            execution_time = end_time - start_time
            print(f"Array size: {size}, Execution time: {execution_time:.6f} seconds")

# Searching algorithms comparison
def compare_searching_algorithms() -> None:
    """
    Compare the performance of different searching algorithms on sorted and unsorted arrays.
    """
    searching_algorithms = {
        'Linear Search': linear_search,
        'Binary Search': binary_search,
        'Interpolation Search': interpolation_search,
        'Exponential Search': exponential_search,
        'Jump Search': jump_search
    }

    array_sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]

    for algorithm_name, algorithm_func in searching_algorithms.items():
        print(f"Comparing {algorithm_name}:")

        for size in array_sizes:
            unsorted_array = generate_random_array(size)
            sorted_array = generate_sorted_array(size)
            key = random.randint(1, size)  # Random key within the array size

            start_time_unsorted = time.time()
            result_unsorted = algorithm_func(unsorted_array, key)
            end_time_unsorted = time.time()
            execution_time_unsorted = end_time_unsorted - start_time_unsorted

            start_time_sorted = time.time()
            result_sorted = algorithm_func(sorted_array, key)
            end_time_sorted = time.time()
            execution_time_sorted = end_time_sorted - start_time_sorted

            print(f"Array size: {size}, Unsorted time: {execution_time_unsorted:.6f} seconds, Sorted time: {execution_time_sorted:.6f} seconds")

def main():
    compare_sorting_algorithms()
    compare_searching_algorithms()

if __name__ == "__main__":
    main()
    
