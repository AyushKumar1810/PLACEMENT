# 75. Sort Colors
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

#*NOTE:# we can use the Dutch National Flag algorithm proposed by Edsger W. Dijkstra. This algorithm uses three pointers to partition the array into three sections:

# Elements less than the mid-value (0 in this case)
# Elements equal to the mid-value (1 in this case)
# Elements greater than the mid-value (2 in this case)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low , mid , end = 0 , 0 , len(nums)-1
        while mid<=end:
            if nums[mid]==0:
                nums[low] , nums[mid] = nums[mid] , nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[end] , nums[mid]=nums[mid] , nums[end]
                end-=1
