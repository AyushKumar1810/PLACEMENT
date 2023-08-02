#Question = Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

# Example:
# Input: arr[] = {7, 10, 4, 3, 20, 15}
# k = 3
# Output: 7 .

#NOTE- we will use max heap as we have to find Kth smallest elements , as using maxheap on the top maxi,um element will be there and we will go to kth smallest and return top element and when K>size of max_heap then we will pop the element :
 
import heapq

l = [7, 10, 4, 3, 20, 15]
k = 3
heap = []

# Iterate through the list
for i in range(0, len(l)):
    # Push the negation of the current element into the max heap
    heapq.heappush(heap, -l[i])
    
    # If the heap size exceeds k, remove the largest element
    if len(heap) > k:
        heapq.heappop(heap)

# The top element in the heap is the kth smallest element (negated)
print(-heap[0])


