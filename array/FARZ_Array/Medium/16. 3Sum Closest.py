# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

#NOTE: We will make a loop over array and we will store differnece (arr[[i] - taget) in some array and we will return minimum value that will be claoset one

#Brute Force Solution:
def threeSumClosest(nums, target):
    closet_sum= float('inf')
    min_diff=float('inf')
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1) , len(nums):
            for k in range(j+1 , len(nums)):
                currcurrent_sum=nums[i] + nums[j] + nums[k]
                current_diff=abs(currcurrent_sum-target)
                if current_diff < min_diff:
                    min_diff=current_diff
                    closet_sum=currcurrent_sum

    return closet_sum



#Optimized Solution:
def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    min_diff = float('inf')
    
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            current_diff = abs(current_sum - target)
            
            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum
                
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum
                
    return closest_sum

# Example usage:
nums = [-1, 2, 1, -4]
target = 1
print("Output:", threeSumClosest(nums, target))