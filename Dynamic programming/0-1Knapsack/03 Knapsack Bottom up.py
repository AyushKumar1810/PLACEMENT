def knapsack(wt, val, W, n):
    # Initialize DP matrix
    t = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the matrix in bottom-up manner
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i - 1] <= j:
                t[i][j]= max(val[i - 1] + t[i - 1][j - wt[i - 1]] , t[i-1][j])
            else:
                t[i][j] = t[i - 1][j]

    return t[n][W]
#   0 1 2 3 4 5 6 7
# 0 0 0 0 0 0 0 0 0
# 1 0 1 1 1 1 1 1 1
# 2 0 1 1 4 5 5 5 5
# 3 0 1 1 4 5 6 6 9
# 4 0 1 1 4 5 7 8 9
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    wt = list(map(int, input("Enter weights: ").split()))
    val = list(map(int, input("Enter values: ").split()))
    W = int(input("Enter knapsack capacity: "))
    
    print(knapsack(wt, val, W, n))