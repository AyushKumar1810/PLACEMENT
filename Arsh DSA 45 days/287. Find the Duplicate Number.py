# 287. Find the Duplicate Number
# Solved
# Medium
# Topics
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?

# NOTE=this below is using inbuilt set function
# # class Solution:
# #     def findDuplicate(self,nums):
# #         num_set = set()

# #         for num in nums:
# #             if num in num_set:
# #                 return num
# #             num_set.add(num)

# #         return None

# NOTE=Now using Hash Map
# # # class Solution:

# # #     def findDuplicate(self,nums):
# # #         num_dict = {}

# # #         for num in nums:
# # #             if num in num_dict:
# # #                 return num
# # #             num_dict[num] = True

# # #         return None


# NOTE=Using Floyd's Cycle Detection { Quite Hard Approach}
class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        # Move the pointers until a cycle is detected
        while True:
            slow = nums[slow]  # Move slow pointer one step
            fast = nums[nums[fast]]  # Move fast pointer two steps

            # Check if the pointers meet, indicating a cycle
            if slow == fast:
                slow = 0  # Reset slow pointer to start of the list

                # Find the entry point of the cycle
                while slow != fast:
                    slow = nums[slow]  # Move slow pointer one step
                    fast = nums[fast]  # Move fast pointer one step

                return slow

#For practice 
class Solution:
    def findDuplicate(self, nums):
        slow , fast = 0 , 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                slow = 0
                while slow !=fast:
                    slow=nums[slow]
                    fast=nums[fast]
                return slow