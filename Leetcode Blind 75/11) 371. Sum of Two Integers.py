# 371. Sum of Two Integers
# Given two integers a and b, return the sum of the two integers without using the operators + and -.  

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Constants to handle overflow in a 32-bit signed integer
        MAX = 0x7FFFFFFF  # 2^31 - 1
        mask = 0xFFFFFFFF  # 2^32 - 1

        while b != 0:
            # XOR operation to add without carrying
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # If a is negative in 32-bit signed integer, convert it to Python's int representation
        return a if a <= MAX else ~(a ^ mask)

# Example usage
solution = Solution()
print(solution.getSum(1, 2)) 
print(solution.getSum(2, 3))  


        