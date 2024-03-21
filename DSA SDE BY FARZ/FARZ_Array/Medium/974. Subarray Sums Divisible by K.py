# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0

#NOTE:Here's the step-by-step approach:

# Initialize a hashmap remainder_freq to store the frequency of remainder values encountered so far.
# Initialize sum to 0 and count to 0. These will be used to keep track of the running sum and the total count of subarrays with a sum divisible by k.
# Iterate through each element num in the array nums:
# Update sum by adding num to it.
# Calculate the remainder mod of sum when divided by k.
# If mod is negative, add k to it to make it positive.
# Increment the frequency of mod in remainder_freq.
# Add the frequency of mod to count.
# Return count, which represents the total count of subarrays with a sum divisible by k.

def subarraysDivByK(nums, k):
    remainder_freq = {0: 1}  # Initialize with 0 remainder frequency
    sum, count = 0, 0

    for num in nums:
        sum += num
        mod = sum % k
        if mod < 0:  # Ensure mod is non-negative
            mod += k
        count += remainder_freq.get(mod, 0)
        remainder_freq[mod] = remainder_freq.get(mod, 0) + 1

    return count

# Example usage:
nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
print(subarraysDivByK(nums1, k1))  # Output: 7

nums2 = [5]
k2 = 9
print(subarraysDivByK(nums2, k2))  # Output: 0
