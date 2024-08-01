# 647. Palindromic Substrings
# Hint
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        # Initialize a lookup table of dimensions len(s) * len(s)
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        
        # Base case: A string with one letter is always a palindrome
        for i in range(len(s)):
            dp[i][i] = True
            count += 1

        # Base case: Substrings of two letters
        for i in range(len(s)-1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            # A boolean value is added to the count where True means 1 and False means 0
            count += dp[i][i + 1]

        # Substrings of lengths greater than 2
        for length in range(3, len(s)+1):
            i = 0
            # Checking every possible substring of any specific length
            for j in range(length - 1, len(s)):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                count += dp[i][j]
                i += 1
        
        return count