# Print the elements of an array in the increasing frequency if 2 numbers have same frequency then print the one which came first.

# Example:
# Input : arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
# Output : arr[] = {8, 8, 8, 2, 2, 5, 5, 6} .

#NOTE- We just have to print the Frequnecy in sorted manner . 

import heapq
def frequencySort(arr):
    # Step 1: Create a frequency map using a dictionary
    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    # Step 2: Create a min-heap based on the frequency
    min_heap = []
    for num, freq in freq_map.items():
        # Use negative frequency to create a min-heap instead of max-heap
        heapq.heappush(min_heap, (freq, num))
    
    # Step 3: Build the result array by extracting elements from the min-heap
    result = []
    while min_heap:
        min_freq, num = heapq.heappop(min_heap)
        
        # Add the element to the result array the number of times equal to its frequency
        result.extend([num] * min_freq)
    
    return result
arr = [4, 2, 1, 2, 6, 1, 6, 4, 4, 4]
output = frequencySort(arr)

print("Input:", arr)
print("Output:", output)