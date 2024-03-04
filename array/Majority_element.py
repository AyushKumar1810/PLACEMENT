# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

#NOTE:The Apporach is quite Clear we will store each count and value using HashMap then we will use condition if element in hashmap hreater than [n/2] then we will return it .
# we have Three solution 1. Brute force , 2. Using Boyer-Moore Voting Algorithm) 3. uisng HashMap , 4. Uuisng sorting

#1.Using Brute Force : we will take two Brute Force and we will mke conditions on that 
# A brute force solution for finding the majority element involves checking each element against all other elements to find the one that appears more than ⌊n / 2⌋ times. This solution has a time complexity of O(n^2).

def majority_element_brute_force(nums):
    n = len(nums)
    for num in nums:
        count = sum(1 for i in nums if i == num)
        if count > n // 2:
            return num
    return None

# Example usage:
nums1 = [3, 2, 3]
print(majority_element_brute_force(nums1))  # Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element_brute_force(nums2))  # Output: 2

#2.) Now we will use "Boyer-Moore Voting Algorithm" in that 
def majority_element(nums):
    candidate= None
    count=0
    for num in nums:
        if count ==0:
            candidate = num
        count+=1 if num==candidate else -1
    return candidate
# Example usage:
nums1 = [3, 2, 3]
print(majority_element(nums1))  # Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums2))  # Output: 2

#3.) Now we Will use HashMAp for that :The Apporach is quite Clear we will store each count and value using HashMap then we will use condition if element in hashmap hreater than [n/2] then we will return it .
from collections import Counter
def majority_element(nums):
    counts = Counter(nums)
    for num,count in counts.items():
        if count>len(nums)//2:
            return num
        
# Example usage:
nums1 = [3, 2, 3]
print(majority_element(nums1))  # Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums2))  # Output: 2

#4.) using Sort : just sort the array then the Answer will be in the middle and just return it


def majority_element(nums):
    nums.sort()
    return nums[len(nums)//2]
# Example usage:
nums1 = [3, 2, 3]
print(majority_element(nums1))  # Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums2))  # Output: 2