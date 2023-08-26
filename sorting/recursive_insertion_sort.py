def recursive_insertion_sort(arr, n):
    if n <= 1:
        return
    
    recursive_insertion_sort(arr, n - 1)
    
    key = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
n = len(arr)
recursive_insertion_sort(arr, n)
print("Sorted array:", arr)
