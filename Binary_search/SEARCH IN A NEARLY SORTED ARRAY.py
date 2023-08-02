#QUESTION :
# Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array. Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].

# For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved to previous position.

# Example :
# Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
# Output: 2 
# Output is index of 40 in given array

def searchInNearlySortedArray(arr, k):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        # Check if the middle element is the target
        if arr[mid] == k:
            return mid

        # Check if the element before the middle is the target
        if mid - 1 >= start and arr[mid - 1] == k:
            return mid - 1

        # Check if the element after the middle is the target
        if mid + 1 <= end and arr[mid + 1] == k:
            return mid + 1

        # Adjust the search range based on the comparison with the target
        if arr[mid] > k:
            # If the middle element is greater than the target, ignore the next two elements
            end = mid - 2
        else:
            # If the middle element is smaller than the target, ignore the previous two elements
            start = mid + 2

    # Target not found
    return -1
arr = [1, 3, 2, 4, 5, 7, 6, 8, 9]
k = 6
result = searchInNearlySortedArray(arr, k)
print("Index of target:", result)
