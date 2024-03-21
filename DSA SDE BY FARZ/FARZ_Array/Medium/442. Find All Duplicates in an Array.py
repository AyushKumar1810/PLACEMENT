# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []

#NOTE: we will iterate the array and we will store it into hashmap with value and count and we will return it to it;s given array whose count is 2 , "The question is quite easy as it is given that numbers in array either repeated once or twice "

def findDuplicates(nums):
    seen = set()
    duplicates = []
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# Example usage:
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums1))  # Output: [2, 3]

nums2 = [1, 1, 2]
print(findDuplicates(nums2))  # Output: [1]

nums3 = [1]
print(findDuplicates(nums3))  # Output: []

#Optimized Approach:
# The optimized approach utilizes the fact that all integers in the array are in the range [1, n], where n is the length of the array. This property enables us to use the array itself to mark visited elements.

# Iterate through the array.
# For each element num, consider nums[num - 1] as an index (subtracting 1 because the array is 0-indexed).
# If nums[num - 1] is negative, it means we have visited this index before, so num appears twice. Append num to the result list.
# Otherwise, mark nums[num - 1] as visited by negating its value.
# Return the result list.
# Here's a Python implementation of the optimized approach:

def findDuplicates(nums):
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] *= -1
    return duplicates

# Example usage:
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums1))  # Output: [2, 3]

nums2 = [1, 1, 2]
print(findDuplicates(nums2))  # Output: [1]

nums3 = [1]
print(findDuplicates(nums3))  # Output: []
