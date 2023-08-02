#Question= Given an unsorted array and two numbers x and k, find k closest values to x.
# Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3 .

#NOTE= The brute force solution will be we will substract each index of arr[i] with our given target X and will find the closest 3rd element by compairing it's differences with each others
  ##NOTE= So basic Idea is to take difference and store in a Heap , but which heap we will use  ? as we have to get closest wo we will use Max heap as we want smallest difference value .. 
###NOTE= we have to store it's difference value as well as original value at that time  .
### i.e ""temp=abs(arr[i] - x , arr[i])"" , abs for making our value positive .
#### For ex arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3 ,
#### So arr[0]=10 and x=5 , so abs(arr[0]-5)==5 and arr[0]==10 so out temp will store "temp=(5,10)"

#@@@@NOTE= important thing to note here is why there is need to maintain the heap of pair ?
# We can simply push difference in heap and at the end while returning the answer we can simply subtract that value from X.
# But there is problem !!!
# as we are pushing absolute difference in heap so we cant just add the difference,  there could be possibility that difference is negative.
# So better to have pair maintain heap using difference and its value in array as second element of pair.
# OR
# maintain heap of pair<int,bool> and set the bool is equal to true when difference is negative.
# Ans while returning add that value to X if bool is set.

import heapq

def printKClosestNumbers(arr, k, x):
    # Create an empty max heap
    maxHeap = []

    # Iterate through each element in the array
    for num in arr:
        # Calculate the absolute difference between the element and x
        diff = abs(x - num)

        # Add the tuple (diff, num) to the max heap
        heapq.heappush(maxHeap, (diff, num))

        # If the max heap size exceeds k, remove the largest element
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)

    # Print the remaining elements in the max heap (k closest numbers)
    while maxHeap:
        print(maxHeap[0][1])
        heapq.heappop(maxHeap)
