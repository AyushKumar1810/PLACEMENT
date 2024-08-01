# 76. Minimum Window Substring
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = [0] * 128

        for i in t:
            mp[ord(i)] += 1

        count = len(t)
        i = j = 0
        n = len(s)
        minLen = float('inf')
        minStart = 0

        while j < n:
            if mp[ord(s[j])] > 0:
                count -= 1

            mp[ord(s[j])] -= 1
            j += 1

            while count == 0:
                if j - i < minLen:
                    minLen = j - i
                    minStart = i

                mp[ord(s[i])] += 1
                if mp[ord(s[i])] > 0:
                    count += 1

                i += 1

        return s[minStart:minStart + minLen] if minLen != float('inf') else ""

        
        