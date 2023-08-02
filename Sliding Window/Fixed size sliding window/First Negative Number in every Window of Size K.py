#Question : Given an array and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.

# Example:

# Input:
# 1st example :
 #2(size of window {k})
# 5 (size of an array)
# arr=[-8 2 3 -6 10] , k = 2 
# 2nd example : 
#2(size of window {k})
# 8 (size of an array)
# arr=[12 -1 -7 8 -15 30 16 28]
# k=3

# Output:
# 1>   -8 0 -6 -6
# 2>   -1 -1 -7 -15 -15 0 . 

#NOTE-:Gist of the logic used:-

# 1. We're creating a list to store all the negative elements of a current window. At a particular point of time, the list holds negative numbers which are there in the current running window and not all the negative elements in the array. So, that we can retrieve first negative number from the current window.
# 2. When we reached the window size, we need to perform two operations:-
# -> First, we have to retrieve the answer that is the first negative number from the current window. We're checking if the list is empty or not. If it is empty, then there is no negative number in the current window. In that case we'll push 0 in the vector.
# If it's not empty, then the first element in the list is the first negative number of the current window., pushing that into the vector.
# -> Second, we need to slide the window. For that we need to remove the first element of the current window, and add the next element from the array to the window. But before removing the first element, we need to check whether it belongs to the list or not. If it belongs to the list, we need to remove it from the list, as it will not be a part of our next window. So, if the first element is found to be a negative number, then we have to remove it from the list, and this number is happened to be the front element of the list. Then, incrementing the values of i and j to slide the window.

def findFirstNegative(arr, k):
    n = len(arr)
    res = []  # List to store the first negative numbers in each window

    # Initialize variables
    i = 0  # Start index of the window
    j = 0  # End index of the window

    while j < n:
        # If the window size reaches k, find the first negative number
        if j - i + 1 == k:#In summary, the condition j - i + 1 == k is used to determine when the window size has reached k and it's time to find the first negative number within that window. It ensures that the correct window size is considered for the analysis.
            neg_index = -1  # Index of the first negative number in the window

            # Find the first negative number in the current window
            for idx in range(i, j + 1):
                if arr[idx] < 0:
                    neg_index = idx
                    break

            # Add the first negative number (or 0 if none found) to the result list
            res.append(arr[neg_index] if neg_index != -1 else 0)

            # Slide the window by incrementing the start index
            i += 1

        # Expand the window by incrementing the end index
        j += 1

    return res

arr = [2, -3, 4, -6, 5, -1, 4, -2, 3]
k = 3
result = findFirstNegative(arr, k)
print("First Negative Numbers in each Window of Size", k, ":", result)

