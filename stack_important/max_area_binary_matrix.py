
def maxareanbinarymatrix(matrix):
    row=len(matrix)
    col=len(matrix[0])
    heights=[0]*col
    max_area=0
    def calculateHistogramArea(heights):
        stack=[]
        area=0
        i=0
        while i < len(heights):
            if not stack or  heights[i] >=heights[stack[-1]]:
                stack.append(i)
                i=i+1
            else:
                top=stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area=max(area,heights[top]*width)
        while stack:
            top=stack.pop()
            if not stack:
                width=i
            else:
                width=len(heights) - stack[-1] - 1
            area=max(area,heights[top]*width)
        return area
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                heights[j]=0
            else:
                heights[j]=heights[j] + 1
        area=calculateHistogramArea(heights)
        max_area=max(max_area,area)
    return max_area

matrix = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
print(maxareanbinarymatrix(matrix))

# For Finding Subarray of a given matrix

def find_submatrix(matrix, start_row, end_row, start_col, end_col):
    submatrix = []
    for i in range(start_row, end_row + 1):
        row = matrix[i][start_col:end_col + 1]
        submatrix.append(row)
    return submatrix

matrix = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]

submatrix = find_submatrix(matrix, 1, 2, 1, 3)
print(submatrix)
