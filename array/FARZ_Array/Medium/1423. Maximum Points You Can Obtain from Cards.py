# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

# Example 1:

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
# Example 2:

# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always be 4.
# Example 3:

# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. 

def maxScore(cardPoints, k):
    total_points = sum(cardPoints)
    n = len(cardPoints)
    window_size = n - k
    
    window_sum = sum(cardPoints[:window_size])
    min_window_sum = window_sum
    
    for i in range(window_size, n):
        window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_window_sum = min(min_window_sum, window_sum)
    
    return total_points - min_window_sum

# Example usage:
cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
k1 = 3
print(maxScore(cardPoints1, k1))  # Output: 12

cardPoints2 = [2, 2, 2]
k2 = 2
print(maxScore(cardPoints2, k2))  # Output: 4

cardPoints3 = [9, 7, 7, 9, 7, 7, 9]
k3 = 7
print(maxScore(cardPoints3, k3))  # Output: 55
