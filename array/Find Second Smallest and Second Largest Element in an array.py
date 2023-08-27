# #Example 1:
# Input: [1,2,4,7,7,5]
# Output: Second Smallest : 2
# 	Second Largest : 5
# Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

# Example 2:
# Input: [1]
# Output: Second Smallest : -1
# 	Second Largest : -1
# Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.




def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small




def secondLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large




if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]
    n = len(arr)
    sS = secondSmallest(arr, n)
    sL = secondLargest(arr, n)
    print("Second smallest is", sS)
    print("Second largest is", sL)
