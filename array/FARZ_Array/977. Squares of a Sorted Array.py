# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

#NOTE: the approach is quite easy we are concept of binary search nd camparing left with right element but only difference is that we are comparing square of left element with square of right element.
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        left , right , index = 0 , n-1 , n-1
        while left <= right:
            left_square = nums[left]**2
            right_square = nums[right]**2
            if left_square >= right_square:
                result[index] = left_square
                left=left+1
            else:
                result[index] = right_square
                right=right-1
            index = index -1
        return result
    
# Example usage:
solution = Solution()
nums1 = [-4, -1, 0, 3, 10]
print(solution.sortedSquares(nums1))  # Output: [0, 1, 9, 16, 100]

nums2 = [-7, -3, 2, 3, 11]
print(solution.sortedSquares(nums2))  # Output: [4, 9, 9, 49, 121]

#OR simple one:
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums :
            l.append(i*i) # squaring 
        return sorted(l)# the sorting the squaring value