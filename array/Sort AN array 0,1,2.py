# Sort an array of 0s, 1s and 2s | Dutch National Flag problem
# Given an array A[] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.

# This problem is also the same as the famous “Dutch National Flag problem”. The problem was proposed by Edsger Dijkstra. The problem is as follows:

# Given N balls of colour red, white or blue arranged in a line in random order. You have to arrange all the balls such that the balls with the same colours are adjacent with the order of the balls, with the order of the colours being red, white and blue (i.e., all red coloured balls come first then the white coloured balls and then the blue coloured balls). 

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 
def sortColors(nums):
    nums.sort()

# Example usage:
nums1 = [2, 0, 2, 1, 1, 0]
sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]

#NOTE: we will use optimized solution using the Dutch National Flag algorithm:

def sortColors(nums):
    low , mid, high = 0 , 0 , len(nums)-1
    while mid <=high:
        if nums[mid]==0:
            nums[low] , nums[mid] = nums[mid] , nums[low]
            low = low+1
            mid=mid+1
        elif nums[mid]==1:
            mid=mid+1
        else:
            nums[mid] , nums[high] = nums[high] , nums[mid]
            high=high-1
# Example usage:
nums1 = [2, 0, 2, 1, 1, 0]
sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]