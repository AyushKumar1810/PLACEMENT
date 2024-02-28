# Given an array of N integers, and an integer K, the task is to find the number of pairs of integers in the array whose sum is equal to K.

# Examples:  

# Input: arr[] = {1, 5, 7, -1}, K = 6
# Output:  2
# Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

# Input: arr[] = {1, 5, 7, -1, 5}, K = 6
# Output:  3
# Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         


# Input: arr[] = {1, 1, 1, 1}, K = 2
# Output:  6
# Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

# Input: arr[] = {10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1}, K = 11
# Output:  9
# Explanation: Pairs with sum 11 are (10, 1), (10, 1), (10, 1), (12, -1), (10, 1), (10, 1), (10, 1), (7, 4), (6, 5).

#Brute-Force Approach:
def count_pairs_with_sum(arr, K):
    count=0
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] + arr[j]==K:
                count=count+1

    return count
# Example usage:
arr1 = [1, 5, 7, -1]
K1 = 6
print(count_pairs_with_sum(arr1, K1))  # Output: 2

arr2 = [1, 5, 7, -1, 5]
K2 = 6
print(count_pairs_with_sum(arr2, K2))  # Output: 3

#Optimized Approach:
# We can optimize this problem using a hashmap (dictionary in Python) to keep track of the frequency of elements encountered so far. The idea is to iterate through the array once and, for each element arr[i], ""check if K - arr[i] is present in the hashmap"".

def count_pairs_with_sum_optimized(arr, K):
    count=0
    freq_map={}
    for num in arr:
        complement = K-num
        if complement in freq_map:
            count=count+freq_map[complement]
        freq_map[num] = freq_map.get(num,0) +1
    return count
# Example usage:
arr1 = [1, 5, 7, -1]
K1 = 6
print(count_pairs_with_sum_optimized(arr1, K1))  # Output: 2

arr2 = [1, 5, 7, -1, 5]
K2 = 6
print(count_pairs_with_sum_optimized(arr2, K2))  # Output: 3

#Modified OPTIMAL Solution 
def count_pairs_with_sum_easy(arr, K):
    seen = set()
    count=0
    for num in arr:
        complement = K-num
        if complement in seen:
           count=count+1
        seen.add(num)
    return count

# Example usage:
arr1 = [1, 5, 7, -1]
K1 = 6
print(count_pairs_with_sum_easy(arr1, K1))  # Output: 2

arr2 = [1, 5, 7, -1, 5]
K2 = 6
print(count_pairs_with_sum_easy(arr2, K2))  # Output: 3
