#Question - Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers in order of one space.

# Input:[3 1 2 5 3]

# Output:[3, 4] 

# Duplicate = 3, Missing = 4 . 

#NOTE- we can solve this question by taking all the given array into hash map and we will get our No and it's Count ( Hash Map always use when we have to count something) , after that we will traverse Our Hash Map ( for i in range (1,n)) as we have given a array from 1 to N so any no will be in bewteen that , so after traversing we can get duplicate element and misising element 
# 1 > for Missing element we will use ""If arr[i] not in Hash Map Return arr[i]" 
 #2> For duplicate """if our count is greater than 1 Then reaturn it """
# But It will be us time and space complexivity of O(N) , what can we do to reduce space complexivity   to O(1) ?

#NOTE=The space complexity of the function is O(1) because it uses a constant amount of additional space to store the variables n, arr_sum, arr_sum_sq, actual_sum, actual_sum_sq, missing_number, and duplicate_number. The space used does not depend on the size of the input array.


def findMissingAndDuplicate(arr):
    n = len(arr)

    # Calculate the sum of the array elements
    arr_sum = sum(arr)

    # Calculate the sum of squares of the array elements
    arr_sum_sq = sum([x*x for x in arr])

    # Calculate the actual sum using the formula for the sum of numbers from 1 to N
    actual_sum = (n * (n + 1)) // 2 # For calculating N sum is n*(n+1)/2

    # Calculate the actual sum of squares using the formula for the sum of squares of numbers from 1 to N
    actual_sum_sq = (n * (n + 1) * (2 * n + 1)) // 6 # Calculating square of n sum is {n*(n+1)*(2n+1)/6}

    # Calculate the missing number using the derived formula
    missing_number = (actual_sum - arr_sum) + (actual_sum_sq - arr_sum_sq) // (actual_sum - arr_sum)

    # Calculate the duplicate number by subtracting the missing number from the difference of sums
    duplicate_number = missing_number - (actual_sum - arr_sum)

    # Print the results
    print("Missing Number:", missing_number)
    print("Duplicate Number:", duplicate_number)

# Example usage:
arr = [4, 3, 2, 6, 5, 5]
findMissingAndDuplicate(arr)
