# Given an array arr[] of size N and a number K, where K is smaller than the size of the array. Find the K’th smallest element in the given array. Given that all array elements are distinct.

# Examples:  

# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
# Output: 7

# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
# Output: 10 

#BRUTE FORCE APPROCH:In this we wil sort our array and we will return arr[k-1] element tat will be our answer.

def kth_smallest_bf(arr, k):
    # Sort the array
    arr.sort()
    
    # Return the Kth smallest element
    return arr[k-1]

# Example usage:
arr1 = [7, 10, 4, 3, 20, 15]
k1 = 3
print(kth_smallest_bf(arr1, k1))  # Output: 7

arr2 = [7, 10, 4, 3, 20, 15]
k2 = 4
print(kth_smallest_bf(arr2, k2))  # Output: 10

#Efficient solution : We will use Min Heap
import heapq

def kth_smallest_optimized(arr, k):
    # Use heap to get the Kth smallest element
    heap = arr[:k]# Heap will go from 0 to kth element only 
    heapq.heapify(heap)
    
    for i in range(k, len(arr)):# This Loop will go from the k to n-1
        if arr[i] > heap[0]: #We will comapare 1st element of heap with 1st eleemnt of Loop
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
    
    return heap[0]

# Example usage:
arr1 = [7, 10, 4, 3, 20, 15]
k1 = 3
print(kth_smallest_optimized(arr1, k1))  # Output: 7

arr2 = [7, 10, 4, 3, 20, 15]
k2 = 4
print(kth_smallest_optimized(arr2, k2))  # Output: 10

