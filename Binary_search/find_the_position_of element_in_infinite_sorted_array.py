# Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

#NOTE =Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array.
# If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.

# Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element,
# -if it is greater than high index element then copy high index in low index and double the high index.
# -if it is smaller, then apply binary search on high and low indices found.

def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    res = -1
    
    while l <= r:
        mid = l + (r - l) // 2
        
        if nums[mid] == target:
            res = mid
            break
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return res

nums = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
target = 10

result = binary_search(nums, target)
print(result)
