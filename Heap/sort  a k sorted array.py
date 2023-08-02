# Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

# Example:
# Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
# k = 3 
# Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

# NOTE= Nearly sorted

import heapq

def nearlySorted(arr, k):
    l = []  # Initialize an empty list to store the sorted elements
    q = []  # Initialize an empty priority queue
    
    # Iterate over each element in the input array
    for i in range(len(arr)):
        heapq.heappush(q, arr[i])  # Add the current element to the priority queue
        
        if len(q) > k:
            # If the size of the queue exceeds k, remove the smallest element from the queue
            # and append it to the list l, as it has moved k positions away from its sorted position
            l.append(heapq.heappop(q))
    
    # After processing all the elements, there might be some remaining elements in the priority queue
    # which are already sorted. We continue to remove elements from the queue using heapq.heappop
    # and append them to the list l until the queue is empty.
    while q:
        l.append(heapq.heappop(q))
    
    return l


# Example usage
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3

sorted_arr = nearlySorted(arr, k)

print("Input array:", arr)
print("k:", k)
print("Nearly Sorted Array:", sorted_arr)
