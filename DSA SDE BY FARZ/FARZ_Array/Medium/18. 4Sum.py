# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.



# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

#Brute Force Approach:
def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        quad = [nums[a], nums[b], nums[c], nums[d]]
                        if quad not in result:
                            result.append(quad)
    return result

# Example usage:
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
print("Output for nums1:", fourSum(nums1, target1))

nums2 = [2, 2, 2, 2, 2]
target2 = 8
print("Output for nums2:", fourSum(nums2, target2))


# Optimized Approach:
# In the optimized approach, we use a two-pointer technique similar to the 3Sum problem. We sort the array first and then iterate through each element, using two pointers to find the remaining two elements that sum up to the target. This approach avoids duplicate quadruplets by skipping over duplicate elements.


def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

# Example usage:
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
print("Output for nums1:", fourSum(nums1, target1))

nums2 = [2, 2, 2, 2, 2]
target2 = 8
print("Output for nums2:", fourSum(nums2, target2))