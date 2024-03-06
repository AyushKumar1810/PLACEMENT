# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

def subarraySumBruteForce(nums, k):
    count = 0
    n=len(nums)
    for start in range(n):
        sum=0
        for end in range(start,n):
            sum=sum+nums[end]
            if sum==k:
                count=count+1
    return count
# Example usage:
nums1 = [1, 1, 1]
k1 = 2
print(subarraySumBruteForce(nums1, k1))  # Output: 2

nums2 = [1, 2, 3]
k2 = 3
print(subarraySumBruteForce(nums2, k2))  # Output: 2

#Efficient Approach (Using Prefix Sum and Hash Map):
def subarraySum(nums, k):
    count=0
    prefixsum=0
    sum_count={0:1}
    for num in nums:
        prefixsum=num+prefixsum
        if prefixsum-k in sum_count:
            count+=sum_count[prefixsum-k]
        sum_count[prefixsum] = sum_count.get(prefixsum,0)+1
    return count
# Example usage:
nums1 = [1, 1, 1]
k1 = 2
print(subarraySum(nums1, k1))  # Output: 2

nums2 = [1, 2, 3]
k2 = 3
print(subarraySum(nums2, k2))  # Output: 2