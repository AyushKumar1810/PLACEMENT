##QUESTION :Given a bitonic sequence of n distinct elements,
# write a program to find a given element x in the bitonic sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.

# Examples:

# Input :  arr[] = {-3, 9, 8, 20, 17, 5, 1};
#          key = 20
# Output : Found at index 3


def find_element(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        # If the middle element is equal to the target, return its index
        if nums[mid] == target:
            return mid

        # Check if the start half of the array is in ascending order
        if nums[start] <= nums[mid]: # we are simply comparing mid with start index , if mid > start then it is in ascending order otherwise decending order. 
            # If the target is within the range of the start half, narrow the search to the start half
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            # Otherwise, search the end half
            else:
                start = mid + 1
        # If the start half is not in ascending order, the end half must be in ascending order(as it's bitonic array)
        else:
            # If the target is within the range of the end half, narrow the search to the end half
            if nums[mid] <= target <= nums[end]:
                start = mid + 1
            # Otherwise, search the start half
            else:
                end = mid - 1

    # If the target element is not found, return -1
    return -1

# Example usage:

# Input
nums = [1, 3, 8, 10, 15]
target = 12

# Find the element in the bitonic array
index = find_element(nums, target)

# Output
if index != -1:
    print("Element", target, "found at index", index)
else:
    print("Element", target, "not found in the array.")
