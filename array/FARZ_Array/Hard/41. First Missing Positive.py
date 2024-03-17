# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

def first_missing_positive(nums):
    n = len(nums)
    
    # Perform cyclic sort
    i = 0
    while i < n:
        # Ensure that nums[i] is within the range [1, n]
        if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    
    # Find the smallest positive integer missing
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all positive integers are present, return n + 1
    return n + 1

# Test cases
print(first_missing_positive([1, 2, 0]))  # Output: 3
print(first_missing_positive([3, 4, -1, 1]))  # Output: 2
print(first_missing_positive([7, 8, 9, 11, 12]))  # Output: 1
