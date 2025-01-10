# 31. Next Permutation
# Solved
# Medium
# Topics
# Companies
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

# Approach
# 1. Find the first decreasing element from the end of the array
# 2. Find the element which is just greater than the first decreasing element
# 3. Swap the two elements
# 4. Reverse the array from the next element of the first decreasing element to the end of the array
# 5. If the first decreasing element is not found, reverse the whole array
# 6. Done
# Time Complexity: O(n)
# Space Complexity: O(1)
# Where n is the length of the array nums. 
# The time complexity is O(n) because we are doing a single pass over the array nums.
# The space complexity is O(1) because we are not using any extra space.

#* CODE
def nextPermutation(nums):
    n = len(nums)
    ind = -1
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            ind = i
            break
    if ind ==-1:
        nums.reverse()
        return nums
    for i in range(n-1,ind,-1):
        if nums[i] > nums[ind]:
            nums[i],nums[ind] = nums[ind],nums[i]
            break
    nums[ind+1:] =reversed(nums[ind+1:])
    return nums
# Driver code
nums = [1,2,3]
print(nextPermutation(nums)) # [1,3,2]
nums = [3,2,1]
print(nextPermutation(nums)) # [1,2,3]