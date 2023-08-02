#Find the index of first 1 in an infinite sorted array of 0s and 1s  ?
# Given an infinite sorted array consisting 0s and 1s. The problem is to find
#  the index of first ‘1’ in that array. As the array is infinite, therefore it
# is guaranteed that number ‘1’ will be present in the array.

# Example:

# Input : arr[] = {0, 0, 1, 1, 1, 1} 
# Output : 2

##NOTE=The problem is same as Infinite sorted array + 1st occurance of
#  binary sorted array  . 
# CONCEPT=so we will use the concept of infinite sorted aarray and when it get's 
# finite array then we will use binary search and use the concept of 1st
# occurance of target element , here target is 1 as it's binary .

def search(arr, key):
    start = 0
    end = 1
    result = -1
# below is the code for infinite  sorted binary array
    while key > arr[end]:
        if arr[end] < key:
            start = end
            end = end * 2
# code for 1st occurance
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            result = mid
            end = mid - 1
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return result

arr = [0, 0, 1, 1, 1, 1, 1, 1]
key = 1

index = search(arr, key)
print(index)
