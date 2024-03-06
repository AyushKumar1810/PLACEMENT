# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


#1)Here is Brute Force:
def maxProfitBruteForce(prices):
    max_Profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[j] > prices[i]:
                max_Profit=max(max_Profit,prices[j]-prices[i])
    return max_Profit
prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfitBruteForce(prices1))  # Brute Force

prices2 = [1, 2, 3, 4, 5]
print(maxProfitBruteForce(prices2))  # Brute Force

prices3 = [7, 6, 4, 3, 1]
print(maxProfitBruteForce(prices3))  # Brute Force

#2) For efficient SOution 
def maxProfit(prices):
    if not prices:
        return 0
# Here we are using two Pointer Approach
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit
prices1 = [7, 1, 5, 3, 6, 4]
# print(maxProfitBruteForce(prices1))  # Brute Force
print(maxProfit(prices1))  # Efficient

prices2 = [1, 2, 3, 4, 5]
# print(maxProfitBruteForce(prices2))  # Brute Force
print(maxProfit(prices2))  # Efficient

prices3 = [7, 6, 4, 3, 1]
# print(maxProfitBruteForce(prices3))  # Brute Force
print(maxProfit(prices3))  # Efficient
