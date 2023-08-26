#Question:Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.
# Example:

# Input: arr[] = {1, 2, 3, 3}, X = 6
# Output: 3
# All the possible subsets are {1, 2, 3},
# {1, 2, 3} and {3, 3}
def perfectSumMemoized(arr, n, sum, dp):
    if n == 0 and sum > 0:
        return 0
    if sum == 0 and n == 0:
        return 1

    if dp[n][sum] != -1:
        return dp[n][sum]

    if arr[n - 1] <= sum:
        dp[n][sum] = perfectSumMemoized(arr, n - 1, sum - arr[n - 1], dp) + perfectSumMemoized(arr, n - 1, sum, dp) # Everything is same as o-1 knapsack problem but the difference is here we re adding instead of "or" as here we have to find count and in that question we have to only make true or False 
    else:
        dp[n][sum] = perfectSumMemoized(arr, n - 1, sum, dp)

    return dp[n][sum]

def perfectSum(arr, n, sum):
    dp = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
    return perfectSumMemoized(arr, n, sum, dp)

# Usage:
arr = [1, 5, 0, 11, 5, 0]
n = len(arr)
sum = 16
result = perfectSum(arr, n, sum)
print("Output:", result)
