# 1. Two Sum
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

#NOTE: We cam use hashMap to solve the Ptoblem or using two Pointer approach 
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the value and its index
        num_dict = {}
        # Iterate over the list
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            # Check if the complement is in the dictionary
            if complement in num_dict:
                # If found, return the indices
                return [num_dict[complement], index]
            # Otherwise, add the number and its index to the dictionary
            num_dict[num] = index

# Example usage:
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(sol.twoSum([3, 3], 6))          # Output: [0, 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map={}
        for i,n in enumerate(nums):
            difference= target-n
            if difference in prev_map:
                return [prev_map[difference] , i]
            prev_map[n] = i 