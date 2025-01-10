# 229. Majority Element II
# Medium
# Hint
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109


# Follow up: Could you solve the problem in linear time and in O(1) space?

# Approach
# 1. Initialize two variables num1 and num2 to store the two elements whose count is greater than n/3 and their count to 0 
# 2. Initialize two variables count1 and count2 to store the count of the two elements num1 and num2 and iterate over the array nums  
# 3. If the current element is equal to num1 or num2, increment the count of the respective element  
# 4. If the count of the element num1 is 0, update num1 to the current element and increment the count of num1  
# 5. If the count of the element num2 is 0, update num2 to the current element and increment the count of num2 
# 6. If the current element is not equal to num1 or num2, decrement the count of num1 and num2 
# 7. Done
# Time Complexity: O(n)
# Space Complexity: O(1)
# Where n is the length of the array nums.
# The time complexity is O(n) because we are iterating over the array nums.
# The space complexity is O(1) because we are not using any extra space.
# CODE
def majorityElement(nums):
    num1 = num2 = None
    count1 = count2 = 0
    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
        elif count1 == 0:
            num1 = num
            count1 += 1
        elif count2 == 0:
            num2 = num
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    return [num for num in (num1,num2) if nums.count(num) > len(nums)//3]

# Driver code
nums = [3,2,3]
print(majorityElement(nums)) # [3] 
nums = [1]
print(majorityElement(nums)) # [1]
nums = [1,2]
print(majorityElement(nums)) # [1,2

