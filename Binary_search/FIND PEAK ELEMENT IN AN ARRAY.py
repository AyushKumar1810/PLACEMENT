# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1],
#  find a peak element and return its index.

# The array may contain multiple peaks, in that case return 
# the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example :

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the
#  index number 2.


def find_peak_element(arr):
    start = 0
    end = len(arr) - 1
    ans = 0

    # Check if the array has only one element
    if len(arr) == 1:
        return 0

    # Perform binary search to find the peak element
    while start <= end:
        mid = start + (end - start) // 2

        # Check if the mid index is not at the boundaries of the array
        if mid > 0 and mid < len(arr) - 1:
            # Check if the mid element is greater than its neighboring elements
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            # If the mid element is smaller than its next element, move the start pointer to mid + 1
            elif arr[mid] < arr[mid + 1]:
                start = mid + 1
            # If the mid element is smaller than its previous element, move the end pointer to mid - 1
            else:
                end = mid - 1
        else:
            # Handle the cases when the mid index is at the start or end of the array
            if mid == 0:# if mid is at 0th index then only we have to comapare it with 1st index i.e mid +1
                # If the mid element is greater than its next element, it is a peak
                if arr[mid] > arr[mid + 1]:
                    return mid
                # Otherwise, the peak element must be at the next index
                else:
                    return mid + 1
            elif mid == len(arr) - 1:
                # If the mid element is greater than its previous element, it is a peak
                if arr[mid] > arr[mid - 1]:
                    return mid
                # Otherwise, the peak element must be at the previous index
                else:
                    return mid - 1

    return ans

# Example usage
arr = [1, 2, 3, 1]
result = find_peak_element(arr)
print(result)
