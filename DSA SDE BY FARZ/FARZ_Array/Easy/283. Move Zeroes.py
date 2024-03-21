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

#1.) Brute Force:
def moveZeroes(nums):
    count = 0
    n = len(nums)
    
    # Count the number of non-zero elements
    for num in nums:
        if num != 0:
            count += 1
    
    # Remove non-zero elements from the array
    nums[:] = [num for num in nums if num != 0]
    
    # Append zeroes at the end
    nums += [0] * (n - count)


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)

#2.) Optimal solutions
#NOTE:The efficient approach involves using a two-pointer technique. We maintain two pointers, one for iterating through the array, and the other for placing non-zero elements in their correct positions.

def moveZeroes(nums):
    non_zero_index = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero
        if nums[i] != 0:
            # Swap the non-zero element with the first zero encountered
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1
# For the given input array
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)