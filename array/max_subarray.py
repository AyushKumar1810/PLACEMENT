# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
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

# 1.)Brute Force;
def max_subarray_sum(nums):
    n=len(nums)
    max_sum=float('-inf')
    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum=current_sum + nums[j]
            max_sum=max(max_sum,current_sum)
    return max_sum
# Brute-Force Approach
nums_bruteforce = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_bruteforce = max_subarray_sum(nums_bruteforce)
print(f"Brute-Force Output: {result_bruteforce}")
#NOTE: Here Time complexivity is O(n^2) so we will reduce By using (Kadane's Algorithm) 
def max_subarray_sum(nums):
    n = len(nums)
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, n):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
# Efficient Solution (Kadane's Algorithm)
nums_efficient = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_efficient = max_subarray_sum(nums_efficient)
print(f"Efficient Output: {result_efficient}")

#NOTE: Here Time complexivity is O(N) .The efficient solution (Kadane's Algorithm) has a single loop, iterating through the array once, making it O(n). It keeps track of the maximum sum subarray ending at each position.