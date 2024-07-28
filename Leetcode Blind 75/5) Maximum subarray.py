# 53. Maximum Subarray
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum=max_sum = nums[0] # here we are initialising it 
        for num in nums[1:]:# we are iterating from 1st index 
            currentsum=max(num,currentsum+num) # comparing with current index value with all the sum value till that index
            max_sum=max(currentsum,max_sum)
        return max_sum
sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(sol.maxSubArray([1]))  # Output: 1
print(sol.maxSubArray([5, 4, -1, 7, 8]))  # Output: 23

# from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         current_sum = max_sum = nums[0]
#         for num in nums[1:]:
#             current_sum=max(num , current_sum+num)
#             max_sum=max(current_sum , max_sum)
#         return max_sum