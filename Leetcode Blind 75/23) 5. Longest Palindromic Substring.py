# 5. Longest Palindromic Substring
# Hint
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
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
    
        start, end = 0, 0
    
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)    # Odd length palindromes
            len2 = expandAroundCenter(s, i, i + 1) # Even length palindromes
            max_len = max(len1, len2)
        
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
    
        return s[start:end + 1]

def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
