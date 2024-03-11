# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(matrix):
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right along the top boundary
        result.extend(matrix[top][left:right + 1])
        top += 1

        # Traverse from top to bottom along the right boundary
        result.extend(matrix[top:bottom + 1][right])
        right -= 1

        # Traverse from right to left along the bottom boundary
        if top <= bottom:
            result.extend(matrix[bottom][left:right + 1][::-1])
            bottom -= 1

        # Traverse from bottom to top along the left boundary
        if left <= right:
            result.extend(matrix[top:bottom + 1][left][::-1])
            left += 1

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiralOrder(matrix))

#NOTE:Initialize Boundaries:

# Define four variables top, bottom, left, and right to represent the boundaries of the untraversed matrix.
# Initially, set top = 0, bottom = len(matrix) - 1, left = 0, and right = len(matrix[0]) - 1.
# Traverse in Spiral Order:

# Use a while loop to traverse the matrix until the boundaries meet.
# Traverse from left to right along the top boundary (matrix[top][left:right+1]).
# Increment top to exclude the top row from further traversal.
# Traverse from top to bottom along the right boundary (matrix[top:bottom+1][right]).
# Decrement right to exclude the rightmost column from further traversal.
# Traverse from right to left along the bottom boundary (matrix[bottom][left:right+1][::-1]).
# Decrement bottom to exclude the bottom row from further traversal.
# Traverse from bottom to top along the left boundary (matrix[top:bottom+1][left][::-1]).
# Increment left to exclude the leftmost column from further traversal.
# Repeat Until Boundaries Meet:

# Continue these steps until top is greater than bottom or left is greater than right.
# Return Result:

# The result is the elements traversed in the spiral order.