# Given an array of n numbers. Your task is to read numbers from the array and keep at-most K numbers at the top (According to their decreasing frequency) every time a new number is read. We basically need to print top k numbers sorted by frequency when input stream has included k distinct elements, else need to print all distinct elements sorted by frequency.

# Example:
# Input :  arr[] = {5, 2, 1, 3, 2}
# k = 4
# Output : 5 2 5 1 2 5 1 2 3 5 2 1 3 5 . 

#NOTE= the idea we are using it's that , we are first using hash map for counting frequency of each Given element and after that we will get ( frequency , Value )
# for eg [1, 1, 1, 3, 2, 2, 4, 4, 4]  After hash map we will get 
# {1: 3, 3: 1, 2: 2, 4: 3} . Next, we create a min heap and push the (frequency, element) pairs onto it: After that when len(min_heap)>k we pop out Top element and last 2 element will remain adn we will return it ,, . [(3, 1), (3, 4)] 4 occurs 3 times and 1 occurs 3 times . as we can see it 


import heapq

def topKFrequent(nums, k):
    # Step 1: Create a frequency map using a hash map
    freq_map = {}  # Hash map to store the frequencies of elements

    # Count the frequencies of elements in the input list
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1 # If num is already There then increament the counter by 1 
        else:
            freq_map[num] = 1

    # Step 2: Create a min heap of size k using the heapq module
    min_heap = []

    # Push the (frequency, element) pairs onto the min heap
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))

        # If the size of the min heap exceeds k, remove the element with the lowest frequency
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Extract the k most frequent elements from the min heap
    top_k = []

    # Extract the elements from the min heap and append them to the top_k list
    while min_heap:
        freq, num = heapq.heappop(min_heap)
        top_k.append(num)

    # Return the k most frequent elements in descending order of frequency
    return top_k[::-1]

# Example usage:
nums = [1, 1, 1, 3, 2, 2, 4, 4, 4]
k = 2

result = topKFrequent(nums, k)
print(result)


