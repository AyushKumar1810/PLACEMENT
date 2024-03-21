# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 
# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 

#Here's the step-by-step approach:

# Initialize a variable max_position to 0, which represents the furthest position we can reach.
# Iterate through each element num and index i in the array nums:
# Update max_position as the maximum of max_position and i + nums[i], which represents the furthest position we can reach from the current index i.
# If max_position is greater than or equal to the last index of the array, return true, as we can reach the end of the array.
# If the current index i is greater than max_position, it means we cannot reach the current index, so return false.
# If the loop completes without reaching the end of the array, return false.

def canJump(nums):
    max_position = 0
    for i, num in enumerate(nums):
        if i > max_position:
            return False
        max_position = max(max_position, i + num)
        if max_position >= len(nums) - 1:
            return True
    return False

# Example usage:
nums1 = [2, 3, 1, 1, 4]
print(canJump(nums1))  # Output: True

nums2 = [3, 2, 1, 0, 4]
print(canJump(nums2))  # Output: False
