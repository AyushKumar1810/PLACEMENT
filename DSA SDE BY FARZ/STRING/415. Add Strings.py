# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
 

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.


#NOTE:
# Initialize variables:

# result = "" (empty string to store the result)
# carry = 0 (to keep track of the carry)
# i and j are pointers starting from the right end of num1 and num2, respectively.
# Start iterating from the right end of both strings:

# At the first iteration:
# carry += ord('6') - ord('0') (adding the ASCII value of '6' minus the ASCII value of '0' to carry), which equals 6.
# carry += ord('7') - ord('0') (adding the ASCII value of '7' minus the ASCII value of '0' to carry), which equals 13.
# Append the last digit of the sum (carry % 10), which is 3, to the result.
# Set carry to carry // 10, which is 1 (the carry for the next iteration).
# Move pointers i and j to the left.
# Continue the iteration:

# At the second iteration:
# carry += ord('5') - ord('0') (adding the ASCII value of '5' minus the ASCII value of '0' to carry), which equals 5.
# Since num2 has been exhausted, we only need to consider num1.
# Append the last digit of the sum (carry % 10), which is 6, to the result.
# Set carry to carry // 10, which is 0 (no carry for the next iteration).
# Move pointer i to the left.
# Final result:

# After exhausting both num1 and num2, the result will be "533", which is the sum of 456 and 77.

def addStrings(num1: str, num2: str) -> str:
    result = ""
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += ord(num1[i]) - ord('0')
            i -= 1
        if j >= 0:
            carry += ord(num2[j]) - ord('0')
            j -= 1
        result = str(carry % 10) + result
        carry //= 10
    
    return result

# Example usage:
num1 = "456"
num2 = "77"
output = addStrings(num1, num2)
print("Input:", num1, num2)
print("Output:", output)  # Output: "533"