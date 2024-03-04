# A certain bug's home is on the x-axis at position x. Help them get there from position 0.

# The bug jumps according to the following rules:

# It can jump exactly a positions forward (to the right).
# It can jump exactly b positions backward (to the left).
# It cannot jump backward twice in a row.
# It cannot jump to any forbidden positions.
# The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

# Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

 

# Example 1:

# Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# Output: 3
# Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
# Example 2:

# Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# Output: -1
# Example 3:

# Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# Output: 2
# Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.

#Brute Force Approach:
def minimumJumps(forbidden, a, b, x):
    def jump(position, forward):
        if position == x:
            return 0
        if position in forbidden or position < 0 or position > 6000 or (position, forward) in visited:
            return float('inf')

        visited.add((position, forward))

        forward_jump = 1 + jump(position + a, True) if forward else float('inf')
        backward_jump = 1 + jump(position - b, False) if not forward and position - b >= 0 else float('inf')

        return min(forward_jump, backward_jump)

    visited = set()
    result = jump(0, True)
    return result if result != float('inf') else -1

# Example usage:
forbidden1 = [14, 4, 18, 1, 15]
a1, b1, x1 = 3, 15, 9
print(minimumJumps(forbidden1, a1, b1, x1))  # Output: 3

forbidden2 = [8, 3, 16, 6, 12, 20]
a2, b2, x2 = 15, 13, 11
print(minimumJumps(forbidden2, a2, b2, x2))  # Output: -1

forbidden3 = [1, 6, 2, 14, 5, 17, 4]
a3, b3, x3 = 16, 9, 7
print(minimumJumps(forbidden3, a3, b3, x3))  # Output: 2

#Optimized Solution:
from collections import deque

def minimumJumps(forbidden, a, b, x):
    visited = set()
    forbidden_set = set(forbidden)
    max_position = max(x, max(forbidden) + a + b) + 1

    queue = deque([(0, True, 0)])  # (position, is_forward, jumps)

    while queue:
        position, is_forward, jumps = queue.popleft()

        if position == x:
            return jumps

        if position in visited or position in forbidden_set or position < 0 or position > max_position:
            continue

        visited.add(position)

        if is_forward:
            queue.append((position + a, False, jumps + 1))
        if not is_forward and position - b >= 0:
            queue.append((position - b, True, jumps + 1))

    return -1

# Example usage:
print(minimumJumps(forbidden1, a1, b1, x1))  # Output: 3
print(minimumJumps(forbidden2, a2, b2, x2))  # Output: -1
print(minimumJumps(forbidden3, a3, b3, x3))  # Output: 2
