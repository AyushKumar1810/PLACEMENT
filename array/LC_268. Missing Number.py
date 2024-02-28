# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

#NOTE: Here we can solve the question By 3 ways
#1.) Brute Force
#2.) Using sum of n natural formula
#3.) UisUsingng XOR technique 
#SOLUTION 1; Simple we iterate the array and we can the length of array as n and number will be in between 0 to n-1 so we will iterarte and those element are not present in that we will return it 

def missingNumber(nums):
    n = len(nums)
    for i in range(n):
        if i not in nums:
            return i
# Example usage:
nums1 = [3, 0, 1]
print(missingNumber(nums1))  # Output: 2

nums2 = [0, 1]
print(missingNumber(nums2))  # Output: 2

nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums3))  # Output: 8
#Time compleivity :This solution is straightforward but has a time complexity of O(N^2), 

#2nd Approch (More efficient One): we will take sum of Given array and we will take sum of "n" natural Number and we will substract "n" natural number with array sum And we will get Unpresent element of that array

def missingNumber(nums):
    n = len(nums)
    
    # Calculate the sum of the first n natural numbers using the formula n * (n + 1) / 2
    expected_sum = n * (n + 1) // 2
    
    # Calculate the sum of the elements in the array
    actual_sum = sum(nums)
    
    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum

# Example usage:
nums1 = [3, 0, 1]
print(missingNumber(nums1))  # Output: 2

nums2 = [0, 1]
print(missingNumber(nums2))  # Output: 2

nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums3))  # Output: 8

#Approach 3 Uisng Xor , As we know That Xor of same element is 0 and Xor of different element is 1 , so basically we will Xor num with it's length n , if we got 1 then that elemet is Notprsenet

def missingNumber(nums):
    n = len(nums)
    
    # Initialize the result with the length of the array
    result = n
    
    # XOR each element and its index
    for i in range(n):
        result ^= i
        result ^= nums[i]
    
    return result

# Example usage:
nums1 = [3, 0, 1]
print(missingNumber(nums1))  # Output: 2

nums2 = [0, 1]
print(missingNumber(nums2))  # Output: 2

nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums3))  # Output: 8
