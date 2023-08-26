#NOTE:Approach:

# Now, let’s understand how we are going to implement the logic of the above steps. In the intuition, we have seen that the given array should be broken down into subarrays. But while implementing, we are not going to break down and create any new arrays. Instead, we will specify the range of the subarrays using two indices or pointers(i.e. low pointer and high pointer) each time while breaking down the array.

# The algorithm steps are the following for the quickSort() function:

# Initially, the low points to the first index and the high points to the last index(as the range is n i.e. the size of the array). 
# After that, we will get the index(where the pivot should be placed after sorting) while shifting the smaller elements on the left and the larger ones on the right using a partition() function discussed later.
# Now, this index can be called the partition index as it creates a partition between the left and the right unsorted subarrays.
# After placing the pivot in the partition index(within the partition() function specified), we need to call the function quickSort() for the left and the right subarray recursively. So, the range of the left subarray will be [low to (partition index – 1)] and the range of the right subarray will be [(partition index + 1) to high]. 
# This is how the recursion will continue until the range becomes 1.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
