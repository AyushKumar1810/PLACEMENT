# Question - There are given n ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths. We need to connect the ropes with minimum cost.

# For example if we are given 4 ropes of lengths 4, 3, 2 and 6. We can connect the ropes in following ways.
# 1) First connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6 and 5.
# 2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
# 3) Finally connect the two ropes and all ropes have connected.

# Total cost for connecting all ropes is 5 + 9 + 15 = 29. This is the optimized cost for connecting ropes. Other ways of connecting ropes would always have same or more cost. For example, if we connect 4 and 6 first (we get three strings of 3, 2 and 10), then connect 10 and 3 (we get two strings of 13 and 2). Finally we connect 13 and 2. Total cost in this way is 10 + 13 + 15 = 38. . 

#NOTE-So we will make a min heap and sort our element in  it after that we will take out two top element and add them and store in "temp" variable and take into another variable  called "ans " . After that we will add to that min_heap and again heapify and the proces countinue till we have 2 element . 


import heapq

def findMinCost(arr):
    heap = []  # Create an empty heap
    ans = 0  # Initialize the answer variable

    # Push all elements from the array to the heap
    for x in arr:
        heapq.heappush(heap, x)

    # Merge elements until only one element remains in the heap
    while len(heap) != 1:
        x1 = heapq.heappop(heap)  # Pop the smallest element from the heap
        x2 = heapq.heappop(heap)  # Pop the second smallest element from the heap

        temp = x1 + x2  # Merge the two elements
        ans += temp  # Update the answer by adding the merged value
        heapq.heappush(heap, temp)  # Push the merged value back into the heap

    return ans  # Return the minimum cost

# Test the function
arr = [2, 3, 4, 1, 5]
min_cost = findMinCost(arr)
print("Minimum Cost:", min_cost)


 
