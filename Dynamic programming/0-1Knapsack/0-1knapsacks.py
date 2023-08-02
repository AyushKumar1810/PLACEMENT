#NOTE: so we have to do few things for solving our Dp problem :
#1.After Making A Matrix we will initialize every entity to -1 and then we will check if any value is present except -1 then we will return that value :
#2. if weight of any index is less than given weight so we will check the maximum value in between when we select that value or when we will not select that value then we will update our matrix accordingly 
def knapSack(W, wt, val, n):
    # Create a 2D array to store the results of subproblems
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    # Helper function to solve the knapsack problem
    def utilKnapSack(W, wt, val, n):
        # Base case: If the capacity of knapsack is 0 or no items left, return 0
        if W == 0 or n == 0:
            memo[n][W] = 0
            return 0
        
        # Check if the result for this subproblem is already computed and stored in the memo 2D array
        if memo[n][W] != -1:
            return memo[n][W]
        
        # If the weight of the current item is less than or equal to the capacity of the knapsack
        # We have two choices: include the item or exclude it
        if wt[n - 1] <= W:
            # Calculate the maximum value by either including or excluding the current item
            included = val[n - 1] + utilKnapSack(W - wt[n - 1], wt, val, n - 1)
            excluded = utilKnapSack(W, wt, val, n - 1)
            # Take the maximum of the two choices and store the result in the memo 2D array
            memo[n][W] = max(included, excluded)
            return memo[n][W]
        else:
            # If the weight of the current item is greater than the capacity of the knapsack
            # We can only exclude the item, so calculate the result for the next subproblem
            memo[n][W] = utilKnapSack(W, wt, val, n - 1)
            return memo[n][W]

    # Call the helper function with the initial parameters and return the result
    return utilKnapSack(W, wt, val, n)
W = 50              # Knapsack capacity
wt = [10, 20, 30]   # List of item weights
val = [60, 100, 120] # List of item values
n = len(wt)         # Number of items

# Calculate the maximum value that can be put in the knapsack
result = knapSack(W, wt, val, n)

print("Maximum value in the knapsack:", result)
