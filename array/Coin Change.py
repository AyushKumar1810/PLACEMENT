# LEETCODE 322. Coin Change
# Medium
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

#1.) Brutte Approach:
def coinChangeBruteForce(coins, amount):
    def dfs(remaining_amount):
        if remaining_amount == 0:
            return 0
        if remaining_amount < 0:
            return float('inf')
        
        min_coins = float('inf')
        for coin in coins:
            result = dfs(remaining_amount - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        return min_coins
    
    result = dfs(amount)
    return result if result != float('inf') else -1

# Example 1:
result1_bruteforce = coinChangeBruteForce([1,2,5], 11)
print(f"Example 1 Brute Force Output: {result1_bruteforce}")

# # Example 2:
# result2_bruteforce = coinChangeBruteForce(coins2, amount2)
# print(f"Example 2 Brute Force Output: {result2_bruteforce}")

# # Example 3:
# result3_bruteforce = coinChangeBruteForce(coins3, amount3)
# print(f"Example 3 Brute Force Output: {result3_bruteforce}")

#2.) Efficient Solutions
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example 1:
result1 = coinChange([2, 5, 10], 27)
print(f"Example 1 Output: {result1}")

# Example 2:
# result2 = coinChange(coins2, amount2)
# print(f"Example 2 Output: {result2}")

# # Example 3:
# result3 = coinChange(coins3, amount3)
# print(f"Example 3 Output: {result3}")
