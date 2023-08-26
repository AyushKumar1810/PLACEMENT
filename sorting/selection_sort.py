# Selection sort uses the concept of finding minimuma and then placing it into 1st place .. 
# The Algorithm Follows :
# The algorithm steps are as follows:

# First, we will select the range of the unsorted array using a loop (say i) that indicates the starting index of the range.
# The loop will run forward from 0 to n-1. The value i = 0 means the range is from 0 to n-1, and similarly, i = 1 means the range is from 1 to n-1, and so on.
# (Initially, the range will be the whole array starting from the first index.)
# Now, in each iteration, we will select the minimum element from the range of the unsorted array using an inner loop.
# After that, we will swap the minimum element with the first element of the selected range(in step 1). 
# Finally, after each iteration, we will find that the array is sorted up to the first index of the range. 

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
