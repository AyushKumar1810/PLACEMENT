def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Current element to be compared and inserted into the sorted subarray
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift larger elements to the right
            j -= 1
        
        arr[j + 1] = key  # Insert the current element at the correct position

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)
