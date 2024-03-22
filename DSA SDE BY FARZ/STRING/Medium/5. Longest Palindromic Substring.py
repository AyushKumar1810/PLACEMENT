# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

#NOTE:To find the longest palindromic substring in a given string s, you can use the following approach:

# Iterate through each character in the string s.
# For each character, consider it as the center of a potential palindrome and expand outward to find the longest palindrome around that center.
# Repeat this process for each character and keep track of the longest palindrome found.

def longest_palindromic_substring(s: str) -> str:
    if len(s) < 2:
        return s

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)
        longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)

    return longest_palindrome

# Example usage:
s1 = "babad"
print(longest_palindromic_substring(s1))  # Output: "bab" or "aba"

s2 = "cbbd"
print(longest_palindromic_substring(s2))  # Output: "bb"
