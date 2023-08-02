#Question:Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

# Example:

# Input 1:
#     A = [1, 3, -1, -3, 5, 3, 6, 7]
#     B = 3
# Output 1:
#     C = [3, 3, 5, 5, 6, 7] . 

def maxSlidingWindow(arr, k):
    ans = []  # List to store the maximum elements in each sliding window
    dq = []  # Deque (double-ended queue) to store indices of potential maximum elements
    
    i = 0  # Start index of the current window
    j = 0  # End index of the current window
    
    while j < len(arr):
        # Iterate through the array elements
        
        # Remove indices from the deque that are smaller than the current element
        while dq and arr[dq[-1]] < arr[j]:
            dq.pop() # we will pop all the smaller value compare to arr[j]
        
        dq.append(j)  # Add the current index to the deque , after compariring and reomving only arr[j] will be remaining( which will be max through that window) so will will all to the dq
        
        if j - i + 1 < k:
            # If the window size is less than k, expand the window by incrementing j
            j += 1
        elif j - i + 1 == k:
            # If the window size is equal to k, it's time to find the maximum element in the window
            
            ans.append(arr[dq[0]])  # The maximum element is the front element of the deque
            
            if dq[0] == i:
                # If the front index of the deque is the start index of the window, remove it
                dq.pop(0)
            
            i += 1  # Slide the window by incrementing both i and j
            j += 1
    
    return ans

# Example usage:
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = maxSlidingWindow(arr, k)
print(result)
