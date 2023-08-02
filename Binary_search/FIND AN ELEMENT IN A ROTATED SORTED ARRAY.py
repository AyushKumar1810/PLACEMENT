##QUESTION :Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(startg n).

# Example:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4 


def binary_search(nums, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target: 
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def find_min(nums):
    n = len(nums)
    start = 0
    end = n - 1
    if nums[start] < nums[end]:
        return 0
    while start <= end:
        mid = start + (end - start) // 2
        next_index = (mid + 1) % n
        prev_index = (mid - 1 + n) % n
        if nums[mid] <= nums[next_index] and nums[mid] <= nums[prev_index]:
            return mid
        if nums[mid] <= nums[end]:
            end = mid - 1
        elif nums[start] <= nums[mid]:
            start = mid + 1
    return -1

# NOTE - The above is same as we have done in that "Minimum no of rotation quesyion" till above code but the difference is that we have to Apply binary search in two parts 1st- starting to minimum value index -1 , 2nd-  from the Minimum value to last element . if we got -1 in left side then our target is not prsenet and it may be on the right and vise versa . but if we got -1 on both right and left then element not present .

def search(nums, target):
    min_index = find_min(nums) # stores Minimum value index
    n = len(nums)
    a1 = binary_search(nums, target, 0, min_index - 1) # we are using binary search from 0th index till minimum element that we have found using above code . 
    a2 = binary_search(nums, target, min_index, n - 1) # we are using Binary search From minimum to end of the given array ..
    if a1 == -1: # If it's Not in a1 then it's in a2    
        return a2
    else:
        return a1
nums = [4, 5, 6, 7, 0, 1, 2]
target = 6
result = search(nums, target)
print("Index of target:", result)
