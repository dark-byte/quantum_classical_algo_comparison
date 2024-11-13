# src/classical/sorting.py

def quicksort(arr):
    """
    QuickSort algorithm implementation.
    
    Parameters:
        arr (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    data = [3, 5, 1, 4, 2]
    sorted_data = quicksort(data)
    print(f"Sorted array: {sorted_data}")