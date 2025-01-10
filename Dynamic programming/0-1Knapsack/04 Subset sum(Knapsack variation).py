
# Subset Sum Problem

# Given an array arr[] of non-negative integers and a value sum, the task is to check if there is a subset of the given array whose sum is equal to the given sum. 

# Examples: 

#     Input: arr[] = {3, 34, 4, 12, 5, 2}, sum = 9
#     Output: True
#     Explanation: There is a subset (4, 5) with sum 9.

#     Input: arr[] = {3, 34, 4, 12, 5, 2}, sum = 30
#     Output: False
#     Explanation: There is no subset that add up to 30.

def is_subset_possible(arr, n, sum):
    # Initialize DP matrix
    t = [[False for _ in range(sum + 1)] for _ in range(n + 1)]

    # Initialization
    for i in range(n + 1):
        for j in range(sum + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True

    # Build the matrix in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][sum]

if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    arr = list(map(int, input("Enter the elements: ").split()))
    sum = int(input("Enter the target sum: "))

    if is_subset_possible(arr, n, sum):
        print("Yes")
    else:
        print("No")