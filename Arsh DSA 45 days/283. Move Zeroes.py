# 283. Move Zeroes
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

#NOTE: compare it and swap it to the last if we found 0
def moveZeroes(nums):
    lastnonzerofoundat=0
    for current in range(len(nums)):
        if nums[current]!=0:
            nums[lastnonzerofoundat] , nums[current] = nums[current] , nums[lastnonzerofoundat]
            lastnonzerofoundat+=1
# Example usage
nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [1.2,3]
moveZeroes(nums2)
print(nums2)  # Output: [0]

#practice 
# def moveZeroes(nums):
#     lastzerofound=0
#     for currents in range(len(nums)):
#         if nums[currents]!=0:
#             nums[lastzerofound] , nums[currents] = nums[currents] , nums[lastzerofound]
#             lastzerofound+=1
