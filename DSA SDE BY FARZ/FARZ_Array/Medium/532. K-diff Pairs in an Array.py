# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

 

# Example 1:

# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:

# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

def findPairs(nums, k):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                pairs.add((min(nums[i], nums[j]), max(nums[i], nums[j])))
    return len(pairs)

# Example usage:
nums1 = [3, 1, 4, 1, 5]
k1 = 2
print(findPairs(nums1, k1))  # Output: 2

nums2 = [1, 2, 3, 4, 5]
k2 = 1
print(findPairs(nums2, k2))  # Output: 4

nums3 = [1, 3, 1, 5, 4]
k3 = 0
print(findPairs(nums3, k3))  # Output: 1

#Otimised Solutions
def findPairs(nums, k):
    if k < 0:
        return 0
    
    num_freq = {}
    unique_pairs = 0
    
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1 # If number alredy exits then count inceases otherwise set to 0
    
    for num in num_freq:
        if k == 0:
            if num_freq[num] > 1:
                unique_pairs += 1
        else:
            if num + k in num_freq:
                unique_pairs += 1
    
    return unique_pairs

# Example usage (same as above):
nums1 = [3, 1, 4, 1, 5]
k1 = 2
print(findPairs(nums1, k1))  # Output: 2

nums2 = [1, 2, 3, 4, 5]
k2 = 1
print(findPairs(nums2, k2))  # Output: 4

nums3 = [1, 3, 1, 5, 4]
k3 = 0
print(findPairs(nums3, k3))  # Output: 1
