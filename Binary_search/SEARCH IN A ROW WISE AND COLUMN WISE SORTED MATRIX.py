#QUESTION : Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. The designed algorithm should have linear time complexity.
# Example :

# Input : mat[4][4] = { {10, 20, 30, 40},
#                       {15, 25, 35, 45},
#                       {27, 29, 37, 48},
#                       {32, 33, 39, 50}};
#               x = 29
# Output : Found at (2, 1)

# NOTE-The idea we are using here is that , we have been started with last element
#  of 0th row and 1st index of last coloumn(n-1) . so as it's sorted in ascending 
# oder so left to right increasing , top to bottom increasing .
#  so we have chossen 1st row and last coloumn value , and we will comapare 
# arr[i][j] with the target where i =0 and j=col-1 . then we have three conditions .

#  1st - If it's arr[i][j]==target then return i,j (index) . 2nd= If arr[i][j]>target
#  that means our target is smaller and we have to cjoice either go to the left or go
#  to the downward , as it is sorted and our target is less so we will go to the left
#  instead of downward as downward element is in increasing order , so will will 
#  decrease coloumn value as j=j-1 and row will be same . 3rd= If arr[i][j]<target 
#  then we will definetly go downwards and coloumn will be same but row value will 
#  increamnet as i=i+1 . if we are not getting result return -1



def search_matrix(matrix, target):
    rows = len(matrix)  # Get the number of rows in the matrix
    cols = len(matrix[0])  # Get the number of columns in the matrix

    # Initialize the starting position at the top-right corner of the matrix
    i = 0
    j = cols - 1

    # Perform the search until we go out of bounds
    while i >= 0 and i < rows and j >= 0 and j < cols:
        if matrix[i][j] == target:  # If the current element is equal to the target
            return i, j  # Return the row and column indices
        elif matrix[i][j] < target:  # If the current element is smaller than the target
            i += 1  # Move down to the next row
        else:  # If the current element is larger than the target
            j -= 1  # Move left to the previous column

    return -1, -1  # Target element not found in the matrix, return invalid indices


# Test the function
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 9

# Call the search function and retrieve the indices
row, col = search_matrix(matrix, target)

if row != -1 and col != -1:
    print("Target element", target, "found at row", row, "and column", col)
else:
    print("Target element", target, "not found in the matrix.")

