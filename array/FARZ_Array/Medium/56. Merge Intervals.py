# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
    if not intervals:
        return []

    # Sort intervals based on start times
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        last_start, last_end = merged[-1]

        if current_start <= last_end:  # Overlapping intervals
            merged[-1][1] = max(current_end, last_end)
        else:
            merged.append([current_start, current_end])

    return merged
intervals = [[1,4],[2,3],[8,10],[15,18]]
print(merge(intervals))