#Question -Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers in order of one space.

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# Duplicate = 3, Missing = 4 . 

# We will solve it by swap array , but point to be NOTE Here we can't use swap sort when we have given that our array is constant we can't change it then we have to use our previous appproach or bit maniplutaion 
#NOTE-Iterate through the array and swap each element to its correct position:

#1. For each element, check if it is equal to its corresponding index + 1.
# If it's not, swap the element with the element at its correct position.
# Find the first element that is not at the correct index:

#2>Iterate through the array.
# The element that is not equal to its index + 1 represents the duplicate number.
# Determine the missing number:

#3> The missing number is the index + 1 where the incorrect element should have been.
#4>Print the duplicate and missing numbers.

# By following these steps, we rearrange the elements in the array to their correct positions, allowing us to identify the duplicate and missing numbers.

#NOTE-As the No is given from 1 to n ,but index will be started from o to n-1 , so we get the idea that for every no to be exact place that no should be in place of index i+1 (for eg 1 will be at 0th index {idex value will be array value -1 and when we will go to it's value then it would be definetly index + 1 , 1 inex is 0 so 0 +1 = 1 , and for index value -1 , 1-1=0 [index]}) 

def findMissingAndDuplicate(arr):
    i = 0 # we are starting from index 0
    
    # Put the items at their correct places
    while i < len(arr):#As we can't go beyong the boundary
        if arr[i] != arr[arr[i] - 1]: # we are checking condition if it's node equal means it's eleigible for swap
            # Swap
            val = arr[arr[i] - 1] # stores in temperory variable
            arr[arr[i] - 1] = arr[i] # arr[arr[i] - 1] postion empty so we will stores arr[i] value to it and now arr[i] empty
            arr[i] = val # swap
        else:
            i += 1 # if duplicate exist then we will move to next index by ignoring it 
    
    # Now find the duplicate and missing numbers in the array
    for i in range(len(arr)):
        # If at any index, the element is not the correct one, then that element is the duplicate,
        # and index + 1 is the missing element
        if arr[i] != i + 1:
            duplicate_number = arr[i]
            missing_number = i + 1
            break
    
    # Print the results
    print("Duplicate Number:", duplicate_number)
    print("Missing Number:", missing_number)

# Example usage:
arr = [3, 1, 2, 5, 3]
findMissingAndDuplicate(arr)
