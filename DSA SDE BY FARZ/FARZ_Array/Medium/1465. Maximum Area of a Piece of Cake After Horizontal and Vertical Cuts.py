# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

# horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

 

# Example 1:


# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4 
# Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
# Example 2:


# Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# Output: 6
# Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
# Example 3:

# Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# Output: 9

def maxArea(h, w, horizontalCuts, verticalCuts):
    # Sort the arrays
    horizontalCuts.sort()
    verticalCuts.sort()
    
    # Find maximum distance between consecutive horizontal cuts
    max_horizontal = max(horizontalCuts[0], h - horizontalCuts[-1])
    for i in range(1, len(horizontalCuts)):
        max_horizontal = max(max_horizontal, horizontalCuts[i] - horizontalCuts[i - 1])
    
    # Find maximum distance between consecutive vertical cuts
    max_vertical = max(verticalCuts[0], w - verticalCuts[-1])
    for i in range(1, len(verticalCuts)):
        max_vertical = max(max_vertical, verticalCuts[i] - verticalCuts[i - 1])
    
    # Return the maximum area modulo 10^9 + 7
    return (max_horizontal * max_vertical) % (10**9 + 7)

# Example usage:
h1, w1 = 5, 4
horizontalCuts1 = [1, 2, 4]
verticalCuts1 = [1, 3]
print(maxArea(h1, w1, horizontalCuts1, verticalCuts1))  # Output: 4

h2, w2 = 5, 4
horizontalCuts2 = [3, 1]
verticalCuts2 = [1]
print(maxArea(h2, w2, horizontalCuts2, verticalCuts2))  # Output: 6

h3, w3 = 5, 4
horizontalCuts3 = [3]
verticalCuts3 = [3]
print(maxArea(h3, w3, horizontalCuts3, verticalCuts3))  # Output: 9
