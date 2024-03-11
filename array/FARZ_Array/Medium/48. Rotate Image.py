# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

#Brute Force Solution:
# def rotate(matrix):
#     n = len(matrix)
#     rotated = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             rotated[j][n - i - 1] = matrix[i][j]

#     for i in range(n):
#         for j in range(n):
#             matrix[i][j] = rotated[i][j]
#Optimised solution : solution is super easy we will use 2 steps 
#       1. we will find transpose of that 
#        2. then we will reversed the transposed Matrix and we will get 90 degree turn matrix as comparired to original matrix .
            
def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix in-place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row in-place
    for i in range(n):
        matrix[i].reverse()

# Example input matrix
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Output the original matrix
print("Original Matrix:")
for row in input_matrix:
    print(row)

# Rotate the matrix using the provided function
rotate(input_matrix)

# Output the rotated matrix
print("\nRotated Matrix:")
for row in input_matrix:
    print(row)

                         