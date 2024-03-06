# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from collections import Counter

# def majorityElement(nums):
#     counts = Counter(nums)
#     n = len(nums)

#     for num, count in counts.items():
#         if count > n // 2:

#             return num
# nums = [2,2,1,1,1,2,2]
# print(majorityElement(nums))

# def majorityelements(nums):
#     counts=Counter(nums)
#     n=len(nums)
#     for num , count in counts.items():
#         if count  > n//2:
#             return num

#NOTE:This Below algorithm is known as Boyer-Moore Voting Algorithm. It maintains a count variable to keep track of the majority element. As it traverses through the array, it cancels out each occurrence of a non-majority element with one occurrence of the majority element. When the count becomes zero, it updates the candidate to the current element. The final candidate will be the majority element.
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
