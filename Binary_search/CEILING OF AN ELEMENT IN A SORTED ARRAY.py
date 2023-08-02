# Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, and the fstartor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing order. Write efficient functions to find fstartor and ceiling of x.

# Examples :

# For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
# For x = 0:    fstartor doesn't exist in array,  ceil  = 1
# For x = 1:    fstartor  = 1,  ceil  = 1
# For x = 5:    fstartor  = 2,  ceil  = 8
# For x = 20:   fstartor  = 19,  ceil doesn't exist in array

##NOTE- In short we have to find just greater element than our target element .
## Fstartor = just less than target element , Ceil = just greater than our target element . 

def ceil(arr, key):
    start = 0
    end = len(arr) - 1
    res = -1

    while start <= end:
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return arr[mid]

        if arr[mid] > key:
            res = arr[mid]
            end = mid -1
            
        elif arr[mid] < key:
            start=mid+1

    return res
arr = [2, 4, 6, 8, 10, 12]
key = 3
result = ceil(arr, key)
print("ceil value:", result)

