# 1480. Running Sum of 1d Array
# Easy
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

#1.) BRUTE Approach
def runningSum(nums):
    result = []
    running_sum = 0
    for num in nums:
        running_sum += num
        result.append(running_sum)
    return result

nums = [1, 2, 3, 4]
print(runningSum(nums))

#2>) Efficient Approach : instead of taking extra space {By taking result array} we will use sliding window technique 
def runningSum(nums):
    for i in range(1,len(nums)):
        nums[i] = nums[i] + nums[i-1]# Current value + previous sum
    return nums
nums = [1, 2, 3, 4]
print(runningSum(nums))