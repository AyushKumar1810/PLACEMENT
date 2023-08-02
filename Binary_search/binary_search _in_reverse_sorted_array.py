# In that question we have given an arry which is in decending order... 
#Let's suppose that we have an array sorted in descending order and we want to find index of an element e within this array. Binary search in every step picks the middle element (m) of the array and compares it to e. If these elements are equal, than it returns the index of m. If e is greater than m, than e must be located in the left subarray. On the contrary, if m greater than e, e must be located in the right subarray. At this moment binary search repeats the step on the respective subrarray.
# Because the algoritm splits in every step the array in half (and one half of the array is never processed) the input element must be located (or determined missing) in at most \\log_{2}{n} steps.


##NOTE=The main concept is that the lesser value element will be on the end as 
#it's decending sorted array so when the target value < Mid value so we shift our 
# start vakue to the mid +1 , and if target > mid value so we shift end value
# as end=mid-1




def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end-start)//2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

# Example usage:
nums = [20,17,15,14,13,12,10,8,4,2]
target = 2

index = binary_search(nums, target)
print(index)
