# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

#NOTE: The Approach is quite simple we use two pointer{Left_Product} and {Right_product} . The concept is that if we are at position of arr[i] then we will calculates it's left_product and right product , then as a result we will multiply left_product with right_product . 
def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize arrays to store products to the left and right of each element
    left_products = [1] * n
    right_products = [1] * n
    
    # Calculate products to the left of each element
    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product
    
    # Calculate products to the right of each element
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product
    
    # Calculate the final result
    result = [left_products[i] * right_products[i] for i in range(n)]
    
    return result

# Example usage:
nums1 = [1, 2, 3, 4]
print(productExceptSelf(nums1))

nums2 = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums2))

#Explanation:

# We initialize two arrays (left_products and right_products) to store the product of elements to the left and right of each element, respectively.

# We calculate the products to the left of each element and store them in the left_products array.

# We calculate the products to the right of each element and store them in the right_products array.

# We then calculate the final result by multiplying the corresponding elements from left_products and right_products.

# This solution runs in O(n) time complexity and does not use division. It provides the correct output for the given examples.