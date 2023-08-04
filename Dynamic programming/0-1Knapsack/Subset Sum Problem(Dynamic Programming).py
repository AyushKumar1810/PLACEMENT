#Question :Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# Example:

# Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.

#NOTE: In that we have To make a subsets that will give t sum equal to target sum .. (It can be countinuous or not )
#NOTE to myself : We have to decrease the number of elements by 1 in both Inclusion and exclusion!   Inclusion means, we take current element and start to identify the possible solutions for the remaining sum with rest of the elements!
# Exclusion means, we discard the current element and start to identify the possible solutions for the same sum with rest of the elements excluding the current one
# Here instead of W we have sum so we will make a matrix of size t[n+1][sum+1]
#NOTE:The main idea is to make all value of Matrix To false and then making 1,2,3,4,5,6,7,8,9, and 0th coloumn To true and then checking conditions ..and we also see that 0th coloumn and every row is always true and only one  Given i.e sums sowe will tke weight array as sum 
def subsetSum(arr, sum, n):
    dp = [[False for j in range(sum + 1)] for i in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the table using bottom-up approach
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][sum]

if __name__ == "__main__":
    arr = [2, 3, 7, 8, 10]
    sum = 6
    n = len(arr)
    print("Is the sum present in the subset?", subsetSum(arr, sum, n))

