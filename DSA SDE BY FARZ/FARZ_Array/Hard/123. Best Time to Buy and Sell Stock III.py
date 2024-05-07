# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 105

def maxProfit(prices):
    # Initialize variables to keep track of maximum profit
    buy1 = buy2 = float('-inf')  # Initially set to negative infinity to ensure proper updates
    sell1 = sell2 = 0  # Initially set to 0, as no profit is earned yet
    
    # Iterate through each price in the prices array
    for price in prices:
        # Update buy1: maximum profit after the first buy
        buy1 = max(buy1, -price)  # Take the maximum between current buy1 and the negative of the price
        
        # Update sell1: maximum profit after the first sell
        sell1 = max(sell1, buy1 + price)  # Take the maximum between current sell1 and buy1 + price
        
        # Update buy2: maximum profit after the second buy
        buy2 = max(buy2, sell1 - price)  # Take the maximum between current buy2 and sell1 - price
        
        # Update sell2: maximum profit after the second sell
        sell2 = max(sell2, buy2 + price)  # Take the maximum between current sell2 and buy2 + price
    
    # Return the maximum profit achieved after completing two transactions
    return sell2
