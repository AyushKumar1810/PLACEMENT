# Given an array arr[] of positive numbers, The task is to find the maximum sum of a subsequence such that no 2 numbers in the sequence should be adjacent in the array.

# Examples: 

# Input: arr[] = {5, 5, 10, 100, 10, 5}
# Output: 110
# Explanation: Pick the subsequence {5, 100, 5}.
# The sum is 110 and no two elements are adjacent. This is the highest possible sum.

# Input: arr[] = {3, 2, 7, 10}
# Output: 13
# Explanation: The subsequence is {3, 10}. This gives sum = 13.
# This is the highest possible sum of a subsequence following the given criteria

def max_sum_no_adjacent(arr):
    if not arr:
        return 0

    include, exclude = arr[0], 0

    for i in range(1, len(arr)):
        new_include = exclude + arr[i]
        new_exclude = max(include, exclude)

        include, exclude = new_include, new_exclude

    return max(include, exclude)

# Example usage:
arr1 = [5, 5, 10, 100, 10, 5]
print(max_sum_no_adjacent(arr1))  # Output: 110

arr2 = [3, 2, 7, 10]
print(max_sum_no_adjacent(arr2))  # Output: 13
