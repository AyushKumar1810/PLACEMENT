def count_subsets_with_sum(arr, n, sum):
    # Initialize DP matrix
    t = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]

    # Initialization
    for i in range(n + 1):
        t[i][0] = 1  # When sum is zero, there is always one subset (empty subset)
    for j in range(1, sum + 1):
        t[0][j] = 0  # When array is empty, no subset can have a positive sum

    # Build the matrix in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][sum]

def count_subsets_with_diff(arr, n, diff):
    sum_of_array = sum(arr)

    # Check if (sum_of_array + diff) is even
    if (sum_of_array + diff) % 2 != 0:
        return 0

    target_sum = (sum_of_array + diff) // 2

    return count_subsets_with_sum(arr, n, target_sum)

if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    diff = int(input("Enter the difference: "))

    print(count_subsets_with_diff(arr, n, diff))