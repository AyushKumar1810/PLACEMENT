# 84. Largest Rectangle in Histogram
# Solved
# Hard
# Topics
# Companies
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.


def largestRectangleArea(heights):
    n=len(heights)
    left_smallest = [-1]*n
    right_smallest = [n]*n
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >=heights[i]:
            stack.pop()
        if stack:
            left_smallest[i]=stack[-1]
        stack.append(i)

    stack =[]
    for i in range(n-1,-1,-1):
        while stack and heights[stack[-1]] >=heights[i]:
            stack.pop()

        if stack:
            right_smallest[i]=stack[-1]
            stack.append(i)

    max_area = 0
    for i in range(n):
        width = right_smallest[i]-left_smallest[i] -1
        max_area=max(max_area,width*heights[i])
    return max_area
heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
