# #Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 5
# Explanation: 5 is the largest element in the array. 

# Example2: 
# Input: arr[] = {8,10,5,7,9};
# Output: 10
# Explanation: 10 is the largest element in the array. 

#Approach: 
# Create a max variable and initialize it with arr[0].
# Use a for loop and compare it with other elements of the array
# If any element is greater than the max value, update max value with the element’s value
# Print the max variable.

def findLargestElement(arr , n): 
    max=arr[0]
    for i in range (0,n):
        if max < arr[i]:
            max=arr[i]
    return max
if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = 5
    max = findLargestElement(arr1, n)
    print("The largest element in the array is:", max)


    arr2 = [8, 10, 5, 7, 9]
    n = 5
    max = findLargestElement(arr2, n)
    print("The largest element in the array is:", max)
