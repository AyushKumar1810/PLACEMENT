# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: True.
# Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.


# Example 2:
# Input: N = 5, array[] = {5,4,6,7,8}
# Output: False.
# Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.

# Here element 5 is not smaller than or equal to its future elements.

def sorted(arr,n):
    for i in range(arr,n):
        if arr[i] < arr[i-1]:
            return False
    return True
