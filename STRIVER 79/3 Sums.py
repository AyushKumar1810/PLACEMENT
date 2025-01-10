# 15. 3Sum
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# Approach
# 1. Sort the array
# 2. Iterate over the array and for each element, find the two elements whose sum is equal to the negative of the current element using two pointers approach (left and right pointers)
# 3. Add the triplet to the answer if the sum is equal to 0 and move the pointers accordingly to find the next triplet with the sum equal to 0 
# 4. Done
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Where n is the length of the array nums.
# The time complexity is O(n^2) because we are iterating over the array nums and for each element, we are finding the two elements whose sum is equal to the negative of the current element using the two pointers approach.
# The space complexity is O(1) because we are not using any extra space.
# CODE

def threeSum(nums):
    nums.sort()
    n=len(nums)
    result = []
#     Iterate over the array
    for i in range(n):
#         Skip the duplicates
        if i > 0 and nums[i]==nums[i-1]:
            continue
        # Find the two elements whose sum is equal to the negative of the current element using two pointers approach
        target = -nums[i]
        left , right = i+1, n-1
    #     Iterate over the array using two pointers approach
        while left < right:
            current_sum = nums[left] + nums[right]
    #         Add the triplet to the answer if the sum is equal to 0
            if current_sum == target:
                result.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1
    #      Move the pointers accordingly to find the next triplet with the sum equal to 0 
                while left < right and nums[left] == nums[left-1]:
                    left += 1
#                 Skip the duplicates
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif current_sum < target:
                left+=1
            else:
                right-=1
    return result
# Driver code
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums)) # [[-1,-1,2],[-1,0,1]]
nums = [0,1,1]
print(threeSum(nums)) # []
nums = [0,0,0]
print(threeSum(nums)) # [[0,0,0]]
# Output
# [[-1, -1, 2], [-1, 0, 1]]
# []
# [[0, 0, 0]]
# Time Complexity: O(n^2)
# Space Complexity: O(1)



# def threeSum(nums):
#     nums.sort()
#     n=len(nums)
#     result = []
#     for i in range(n):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         target , left , right = -nums[i], i+1, n-1
#         while left < right:
#             current_sum= nums[left] + nums[right]
#             if current_sum==target:
#                 result.append([nums[i] , nums[left] , nums[right]])
#                 left += 1
#                 right-=1
#                 while left < right and nums[left] == nums[left-1]:
#                     left+=1
#                 while left < right and nums[right] == nums[right+1]:
#                     right-=1
#             elif current_sum < target:
#                 left+=1
#             else:
#                 right-=1
#     return result