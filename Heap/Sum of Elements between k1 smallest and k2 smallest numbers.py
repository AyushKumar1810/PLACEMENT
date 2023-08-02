#Question-Given an array of integers and two numbers k1 and k2. Find the sum of all elements between given two k1’th and k2’th smallest elements of the array. It may  be assumed that all elements of array are distinct.

# Example :
# Input : arr[] = {20, 8, 22, 4, 12, 10, 14},  k1 = 3,  k2 = 6  
# Output : 26          
#          3rd smallest element is 10. 6th smallest element 
#          is 20. Sum of all element between k1 & k2 is
#          12 + 14 = 26 

import heapq

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        p = []  # min heap to find K2-th smallest element
        ans = 0

        # Adding elements to the min heap
        for i in range(N):
            heapq.heappush(p, -A[i])
            if len(p) > K2:
                heapq.heappop(p)

        heapq.heappop(p)  # Removing the K2-th smallest element

        # Accumulating the sum of elements between K1 and K2
        while len(p) > K1:
            ans += -heapq.heappop(p)

        return ans
A = [2, 7, 4, 1, 8, 5]  # List of numbers
N = len(A)  # Size of the list
K1 = 2  # K1 value
K2 = 4  # K2 value

solution = Solution()
output = solution.sumBetweenTwoKth(A, N, K1, K2)

print("Input:")
print("A =", A)
print("N =", N)
print("K1 =", K1)
print("K2 =", K2)

print("\nOutput:")
print("Sum between K1 and K2:", output)
