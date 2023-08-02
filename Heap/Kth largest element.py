# write an efficient program for printing k largest elements in an array. Elements in array can be in any order.

# For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23. . 

#NOTE= we will use Min heap as it's asked for Kth largest element ,,
# As we have to return Top k largest element so we will return min heap instead of printing top element

import heapq
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

nums = [3, 7, 2, 9, 6]
k = 2

kth_largest = findKthLargest(nums, k)

print("Input:", nums)
print("k:", k)
print("Kth Largest Element:", kth_largest)

##2nd sulution 



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in nums:
            print(heap)
            heapq.heappush(heap,i)       #top element of stack will always be minimum
            if len(heap)>k:        
                heapq.heappop(heap)           #if length of stack is more then k then pop top most element fr
                
        return(heapq.heappop(heap))