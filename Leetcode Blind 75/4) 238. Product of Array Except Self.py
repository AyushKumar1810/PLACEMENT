# 238. Product of Array Except Self

# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

#NOTE: we can solve it uisng concepts of prefix multiply and postfix multiply the we will add up Like : suppose we are at arr[i] the, arr[i:] will be postfix and we ill take multiply of that and arr[:i] will be prefix and we will calculate product of prefic and in results we will do sum of prefix  and postfix .

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = [1]*n
        left_product = 1
        for i in range(n):
            ans[i] = left_product
            left_product*=nums[i]
        right_product = 1
        for i in range(n-1,-1,-1):
            ans[i]*=right_product
            right_product*=nums[i]
        return ans
    
#!Practice
# from typing import List
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         product = [1]*n
#         left_product = 1
#         for i in range(n):
#             product[i]=left_product
#             left_product*=nums[i]
#         right_product = 1
#         for i in range(n-1,-1,-1):
#             product[i]*=right_product
#             right_product*=nums[i]
#         return product
    

