
# Count of subsets with sum equal to target

# Given an array arr[] of length n and an integer target, the task is to find the number of subsets with a sum equal to target.

# Examples: 

#     Input: arr[] = [1, 2, 3, 3], target = 6 
#     Output: 3 
#     Explanation: All the possible subsets are [1, 2, 3], [1, 2, 3] and [3, 3]

#     Input: arr[] = [1, 1, 1, 1], target = 1 
#     Output: 4 
#     Explanation: All the possible subsets are [1], [1], [1] and [1]

# Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target.

# Examples:

# Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
# Output: 3
# Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.

# Input: arr[] = [2, 5, 1, 4, 3], target = 10
# Output: 3
# Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.

# Input: arr[] = [5, 7, 8], target = 3
# Output: 0
# Explanation: There are no subsets of the array that sum up to the target 3.

# Input: arr[] = [35, 2, 8, 22], target = 0
# Output: 1
# Explanation: The empty subset is the only subset with a sum of 0.

# Constraints:
# 1 ≤ arr.size() ≤ 103
# 0 ≤ arr[i] ≤ 103
# 0 ≤ target ≤ 103
#NOTE: This problem is same as subsets sum only difference is that there we have to return True or False but here we have to return the count of the subsets , which is int so we will use + sign instead of or operator.
def count_subsets(arr , n , sum):
    t = [[0 for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if i == 0: 
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1
            elif arr[i-1] <= j: 
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]#*here is the only difference , in the subsets sum here we do or operator but there we are doing addition as out Output is int. 
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]
# Test the function
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    sum = int(input("Enter the target sum: "))

    print(count_subsets(arr, n, sum))
# arr = [5, 2, 3, 10, 6, 8]
# target = 16
# n = len(arr)
# print(countSubsets(arr, n, target)) # Output 3