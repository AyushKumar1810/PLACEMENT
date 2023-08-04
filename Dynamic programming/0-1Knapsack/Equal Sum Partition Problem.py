#Question:Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.
# Examples:

# arr[] = {1, 5, 11, 5}
# Output: true 
# The array can be partitioned as {1, 5, 5} and {11}

#NOTE: The idea is that we will go traverse array and finds it's sum if the sum is odd then return false and if it's True then that means we have to find subsets of sum//2..
def can_partition(arr):
    total_sum = sum(arr)
    
    # If the total sum is odd, it's not possible to partition the array into two subsets with equal sums.
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    n = len(arr)
    
    # Initialize a 2D table to store the subproblem results.
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]
    
    # Base case: If the target sum is 0, then an empty subset can be formed.
    for i in range(n + 1):
        dp[i][0] = True
    
    # Dynamic programming to fill the table.
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    # The value at dp[n][target_sum] will be True if there exists a subset with sum equal to target_sum.
    return dp[n][target_sum]

# Example usage:
arr = [1, 5, 11, 5]
result = can_partition(arr)
print("Output:", result)
    
