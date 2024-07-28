# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

#NOTE: we can use several method to solve this :
    #*1st: we will use hashmap and we will return true if we found any repeartaion more than 1
    #*2nd: We can use xor Like we know that xor of likely to be 0 

class Solution:
    def containsDuplicate(self, nums):
        hash_set=set()# defining sets
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
# Example usage:
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))  # Output: true
print(sol.containsDuplicate([1, 2, 3, 4]))  # Output: false
print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: true
        