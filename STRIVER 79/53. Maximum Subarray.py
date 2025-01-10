# 53. Maximum Subarray(Kadane's Algorithm)
# Solved
# Medium
# Topics
# Companies
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

# Approach
# 1. Initialize two variables max_sum and curr_sum to 0 and iterate over the array nums  
# 2. Iterate over the array and for each element, update the curr_sum to the maximum of the current element and the sum of the current element and the previous sum (curr_sum + nums[i]) because the maximum subarray sum ending at the current element will be either the current element or the sum of the current element and the maximum subarray sum ending at the previous element (curr_sum + nums[i]) 
# 3. Update the max_sum to the maximum of the max_sum and the curr_sum because the maximum subarray sum ending at the current element will be either the current element or the maximum subarray sum ending at the previous element (curr_sum) 
# 4. Done 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Where n is the length of the array nums.
# The time complexity is O(n) because we are iterating over the array nums.
# The space complexity is O(1) because we are not using any extra space.
# CODE
def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    for i in range(1,len(nums)):
        curr_sum = max(nums[i],curr_sum+nums[i])
        max_sum = max(max_sum,curr_sum)
    return max_sum
# Driver code
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums)) # 6
# nums = [1]
# print(maxSubArray(nums)) # 1
