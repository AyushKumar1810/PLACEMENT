#question : Problem Description:

# Given an array containing N positive integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.

# For Input:
# 1
# 7 5
# 4 1 1 1 2 3 5
# your output is: 
# 4 . 
#NOTE- As we don't know size of window we have to find siz of the size with respect to Given sum 
#Brute Force : we will take two pointer i and j , Both will be on same position initilaly i,j=0,0 and then we will increament i till we get the required sum ,if we wet the sum rhen we will retrive the length of that j , for finding size we will use {j-1 +1 } and that will be our window and we will increament i
#NOTE: we will invreament j till sum of it is equal to requied sum , we will increament i when our curr sum is equal to sum ..

#NOTE : we have three conditions :
#1. if current sum i < Given sum : 
#                Then we will increament j value , j++ and make sure it will go untill currnt sum == given sum
#2. If currnt sum == given sum :
#                Then we will get it's length by j-i+1 and return it
#3. If currnt sum > given sum:
#                Then we will increament our i value i ++ and mak sure the sum inside i and j should be less than of equal to given sum in short we will do do while not currnt sum  > given sum    

def largestSubarray(arr, k):
    maxLength = 0  # Variable to store the length of the largest subarray with sum equal to k

    i, j = 0, 0  # Pointers to track the start and end indices of the current window
    sum = 0  # Variable to store the sum of elements in the current window

    while j < len(arr):
        sum += arr[j]  # Add the current element to the window sum

        if sum > k:
            # If the window sum becomes greater than k, shrink the window by moving the start index until the sum is no longer greater than k
            while sum > k:
                sum -= arr[i]  # Subtract the element at the start index from the window sum
                i += 1  # Move the start index to the next position

        if sum == k:
            # If the window sum is equal to k, update the maxLength variable by taking the maximum of the previous length and the current length (j - i + 1)
            maxLength = max(maxLength, (j - i + 1))

        j += 1  # Move the end index to the next position to expand the window

    return maxLength
arr = [4, 1, 1, 1, 2, 3, 5]
k = 5
result = largestSubarray(arr, k)
print("Maximum subarray length with sum", k, ":", result)

#The above code is only for handaling postive no . The downward code is for Both postive and negative no

arr = [5, 3, -15, 7, 8, 8, -9]
s = 8

max_length = 0
temp = []
i = 0
j = 0

while j < len(arr):
    # Add the current element to the temporary subarray
    temp.append(arr[j])

    # Check if the sum of the temporary subarray is greater than the target sum
    if sum(temp) > s:
        # Remove elements from the start of the subarray until the sum is less than or equal to the target sum
        while sum(temp) > s:
            temp.pop(0)

    # Check if the sum of the temporary subarray is equal to the target sum
    if sum(temp) == s:
        # Update the maximum length if the current subarray length is greater
        max_length = max(max_length, len(temp))

    # Move the start pointer to the next index
    j += 1

    # Reset the temporary subarray if the end pointer reaches the end of the array
    if j == len(arr):
        temp = []
        i += 1
        j = i

print(max_length)
