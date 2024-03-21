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

def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

# Example usage:
nums1 = [1, 3, 4, 2, 2]
print("Output for nums1:", findDuplicate(nums1))

nums2 = [3, 1, 3, 4, 2]
print("Output for nums2:", findDuplicate(nums2))

nums3 = [3, 3, 3, 3, 3]
print("Output for nums3:", findDuplicate(nums3))

# NOTE=Now using Hash Map
class Solution:

    def findDuplicate(self,nums):
        num_dict = {}
    
        for num in nums:
            if num in num_dict:
                return num
            num_dict[num] = True
    
        return None




#Optimized Approach:
# In the optimized approach, we can use Floyd's Tortoise and Hare algorithm to find the cycle in the array. We treat the array as a linked list where the value at each index represents the next index to jump to. We use two pointers, slow and fast, where slow moves one step at a time and fast moves two steps at a time. When they meet, we reset one of the pointers to the start of the array and move them one step at a time until they meet again. The meeting point will be the duplicate number.

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow

# Example usage:
nums1 = [1, 3, 4, 2, 2]
print("Output for nums1:", findDuplicate(nums1))

nums2 = [3, 1, 3, 4, 2]
print("Output for nums2:", findDuplicate(nums2))

nums3 = [3, 3, 3, 3, 3]
print("Output for nums3:", findDuplicate(nums3))
