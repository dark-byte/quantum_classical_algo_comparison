# src/classical/search.py

def linear_search(arr, target):
    """
    A brute-force linear search algorithm.
    
    Parameters:
        arr (list): The list of elements to search.
        target: The element to find in the list.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    data = [3, 5, 1, 4, 2]
    target = 4
    result = linear_search(data, target)
    print(f"Target {target} found at index: {result}")