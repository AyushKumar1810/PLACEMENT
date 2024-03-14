# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

#Here's the approach:

# Initialize an empty list result to store all subsets.
# Define a recursive function generate_subsets that takes three parameters: index (current index in the array), current_subset (the subset being constructed), and nums (the original array).
# Base case: If index is equal to the length of nums, append a copy of current_subset to result and return.
# Recursive step: In the recursive call, consider two cases:
# Include the current element nums[index] in the subset: Append nums[index] to current_subset, then recursively call generate_subsets with index + 1.
# Exclude the current element nums[index] from the subset: Simply call generate_subsets with index + 1.
# After the recursive calls, return the result list.

def subsets(nums):
    def generate_subsets(index, current_subset, nums):
        if index == len(nums):
            result.append(current_subset[:])  # Append a copy of current_subset to result
            return
        
        # Include the current element in the subset
        current_subset.append(nums[index])
        generate_subsets(index + 1, current_subset, nums)
        
        # Exclude the current element from the subset
        current_subset.pop()  # Backtrack
        generate_subsets(index + 1, current_subset, nums)
    
    result = []
    generate_subsets(0, [], nums)
    return result

# Example usage:
nums1 = [1, 2, 3]
print(subsets(nums1))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

nums2 = [0]
print(subsets(nums2))  # Output: [[], [0]]
