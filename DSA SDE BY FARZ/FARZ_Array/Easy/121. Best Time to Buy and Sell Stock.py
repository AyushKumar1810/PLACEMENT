# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
#NOTE: We itterate the given array and we will take max difference of arr[i] - arr[j] and then thayt we will return the index of that 

#1.) Brute Force Approach
def MaxProfit(prices):
    max_profit=0
    n=len(prices)
    for i in range(n):
        for j in range(i+1 , n):
            profit = prices[j]-prices[i]
            if profit > max_profit:
                max_profit=profit
    return max_profit
prices=[7,6,4,3,1]
prices1=[7,1,5,3,6,4]
print(MaxProfit(prices))
print(MaxProfit(prices1))

#2>:Optimized: Keep track of the minimum price encountered so far and update the maximum profit when a better selling price is found. Time complexity is O(n).
def max_Profit(stock_price):
    min_price=float('inf')
    max_Profit=0
    for price in stock_price:
        min_price=min(min_price,price)
        max_Profit=max(max_Profit,price-min_price)
    return max_Profit
prices1=[7,1,5,3,6,4]
print(MaxProfit(prices1))