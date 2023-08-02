def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end-start)//2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
                                  
    return -1

# Example usage:
nums = [1, 3, 5, 7, 9]
target = 5

index = binary_search(nums, target)
print(index)
