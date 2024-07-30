# 152. Maximum Product Subarray
# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = max_prod=ans=nums[0]
        for num in nums[1:]:
            max_temp = max_prod*num
            min_temp = min_prod*num
            min_prod = min(max_temp , min_temp , num)
            max_prod = max(max_temp , min_temp,num)
            ans = max(ans , max_prod)
        return ans 
solution = Solution()

# Example 1
print(solution.maxProduct([2, 3, -2, 4])) # Output: 6

# Example 2
print(solution.maxProduct([-2, 0, -1])) # Output: 0
