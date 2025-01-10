
# Partition a set into two subsets such that the difference of subset sums is minimum
# Last Updated : 18 Nov, 2024

# Given an array arr[] of size n, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
# If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

# Example: 

#     Input: arr = [1, 6, 11, 5]
#     Output: 1
#     Explanation: S1 = [1, 5, 6], sum = 12,  S2 = [11], sum = 11,  Absolute Difference (12 – 11) = 1

#     Input: arr = [1, 5, 11, 5]
#     Output: 0
#     Explanation: S1 = [1, 5, 5], sum = 11, S2 = [11], sum = 11, Absolute Difference (11 – 11) = 0 

# 2035. Partition Array Into Two Arrays to Minimize Sum Difference
# Hint

# You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

# Return the minimum possible absolute difference.

 

# Example 1:
# example-1

# Input: nums = [3,9,7,3]
# Output: 2
# Explanation: One optimal partition is: [3,9] and [7,3].
# The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

# Example 2:

# Input: nums = [-36,36]
# Output: 72
# Explanation: One optimal partition is: [-36] and [36].
# The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.

# Example 3:
# example-3

# Input: nums = [2,-1,0,4,-2,-9]
# Output: 0
# Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
# The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.

 

# Constraints:

#     1 <= n <= 15
#     nums.length == 2 * n
#     -107 <= nums[i] <= 107

def is_subset_possible(arr, n, total_sum):
    # Initialize DP matrix
    t = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]

    # Initialization
    for i in range(n + 1):
        t[i][0] = True  # A subset with sum 0 is always possible (empty subset)
    for j in range(1, total_sum + 1):
        t[0][j] = False  # No subset can have a positive sum with 0 elements

    # Build the matrix in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
 
    # Collect all subset sums possible with n elements
    subset_sums = []
    for j in range(total_sum + 1): # Check the last row of the matrix for all possible subset sums with n elements 
        if t[n][j]: # If a subset sum is possible, add it to the list of subset sums 
            subset_sums.append(j)  # Add the subset sum to the list of subset sums 

    return subset_sums

def min_subset_sum_diff(arr, n):
    total_sum = sum(arr)

    # Get all possible subset sums
    subset_sums = is_subset_possible(arr, n, total_sum)# Get all possible subset sums with n elements 

    # Find the minimum subset sum difference
    min_diff = float('inf')
    for s in subset_sums:
        min_diff = min(min_diff, abs(total_sum - 2 * s))

    return min_diff

if __name__ == "__main__":
    # n = int(input("Enter number of items: "))
    # arr = list(map(int, input("Enter the elements of the array: ").split()))
    n=4
    arr=[1, 6, 11, 5]

    print(min_subset_sum_diff(arr, n))
#Pracctise 
def is_subsets(arr,n,total_sum):
    t=[[False for _ in range(total_sum+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0]=True
    for i in range(1,total_sum+1):
        t[0][i]=False
    for i in range(1,n+1):
        for j in range(1,total_sum+1):
            if arr[i-1] <=j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    subset_sums = []
    for j in range(total_sum + 1):
        if t[n][j]:
            subset_sums.append(j)
    return subset_sums
def min_subset_sum_diff(arr, n):
    total_sum = sum(arr)
    subset_sums = is_subsets(arr,n,total_sum)
    min_diff = float('inf')
    for s in subset_sums:
        min_diff = min(min_diff, abs(total_sum - 2 * s))
    return min_diff
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    # n=4
    # arr=[1, 6, 11, 5]
    print(min_subset_sum_diff(arr, n )) #Pracctise 
