# 564. Find the Closest Palindrome
# Hard

# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

# The closest is defined as the absolute difference minimized between two integers.

 

# Example 1:

# Input: n = "123"
# Output: "121"
# Example 2:

# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def nearest_palindrome(n):
    num = int(n)
    left, right = num - 1, num + 1

    while True:
        if is_palindrome(left):
            return str(left)
        elif is_palindrome(right):
            return str(right)

        left -= 1
        right += 1

# Example usage:
n1 = "123"
print(nearest_palindrome(n1))  # Output: "121"

n2 = "1"
print(nearest_palindrome(n2))  # Output: "0"
