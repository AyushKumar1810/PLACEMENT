# Problem statement:
# Given a bitonic array find the maximum value of the array.
#  An array is said to be bitonic if it has an increasing sequence of 
# integers followed immediately by a decreasing sequence of integers.

# Example:

# Input:
# 1 4 8 3 2

# Output:
# 8

##NOTE=Basically we have to find the maximum element of the given bitonic array 
# we just have to campare our mid with mid+1 and mid -1 .
# if it's greater than mid + 1 and mid -1 then it will be largest in that array . 
#i.e "if mid > mid +1 and mid > mid -1 then return Mid"
# so it's like a graph of a curve monotonic increasing and monotonic decreasing
#  once it will reach maxima so we just have to get maxima value or index


def find_highest_number(arr):
        # Check if the array has at least 3 elements
    if len(arr) < 3: # as for comparing we need element in the left and right .
        return None

        # Initialize the start and end pointers
    start = 0
    end = len(arr) - 1

        # Perform binary search to find the highest number
    while start <= end:
        mid = (start + end) // 2  # Calculate the middle index

            # Check if the middle element is the highest number
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

            # Check if the middle element is in an increasing part of the array
        elif arr[mid] > arr[mid - 1]:
            start = mid + 1  # Update the start pointer to search in the end half

            # Check if the middle element is in a decreasing part of the array
        else:
            end = mid - 1  # Update the end pointer to search in the start half

    return None  # Return None if the highest number is not found


# Example usage
arr = [1, 2, 3, 4, 5, 2, 0]
result = find_highest_number(arr)
print(result)
