# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

 

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input
# : s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#NOTE : Algorithm:

#1) Initialize a 2D DP array dp of size (len(s) + 1) x (len(t) + 1) with all elements initialized to zero.
#2) Initialize the first row of dp such that dp[0][j] = 0 for all j since there is no way to form any subsequences of t in an empty string s.
#3) Initialize the first column of dp such that dp[i][0] = 1 for all i since there is exactly one way to form an empty subsequence of t in any non-empty string s.
#4) Iterate over s and t using two nested loops:
# 4.i)=>    If s[i-1] == t[j-1], then dp[i][j] = dp[i-1][j-1] + dp[i-1][j].
# 4.ii)=>   If s[i-1] != t[j-1], then dp[i][j] = dp[i-1][j].
#Return dp[len(s)][len(t)], which represents the number of distinct subsequences of t in s.
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s) , len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range (m+1):
            dp[i][0]=1
        for i in range(m+1):
            for j in range(n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]= dp[i-1][j-1]+ dp[i-1][j]
                else :
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]
# Example usage:
sol = Solution()
s = "rabbbit"
t = "rabbit"
print(sol.numDistinct(s, t))  # Output: 3