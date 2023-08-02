##Question --
# Given a sorted array arr[] and a number x, write a function that counts
#  the occurrences of x in arr[].
#  Expected time complexity is O(startgn) .
# Examples:

#   Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
#   Output: 4 // x (or 2) occurs 4 times in arr[]

#   Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
#   Output: 1 

#NOTE= ""The array is  sorted , so our target Num will be toghether . 
# so we have to find the length /count  of our target element"" .
# we can find it's last occurance index and 1st occrance index and then
# we can put toghter as a formula as (Last Occurance - 1st occurance ) + 1 , 
# will give you width / count of our target element...

def count_occurrences(nums, target):
    start = 0  # start pointer
    end = len(nums) - 1  # end pointer
    first_index = -1  # Index of the first occurrence
    last_index = -1  # Index of the last occurrence

    # Find the index of the first occurrence
    while start <= end:
        mid = start + (end - start) // 2  # Calculate the middle index

        if nums[mid] == target:
            first_index = mid
            end = mid - 1  # Search towards the start half (left side) As the first occurance will be definetly on the left side of that if exist ..
            
        elif nums[mid] < target:
            start = mid + 1  # Search towards the end half (right side)
        else:
            end = mid - 1  # Search towards the start half  (left side)

    # Find the index of the last occurrence
    start = 0  # Reset the start pointer
    end = len(nums) - 1  # Reset the end pointer

    while start <= end:
        mid = start + (end - start) // 2  # Calculate the middle index

        if nums[mid] == target:
            last_index = mid
            start = mid + 1  # Search towards the end half
        elif nums[mid] < target:
            start = mid + 1  # Search towards the end half
        else:
            end = mid - 1  # Search towards the start half

    # Calculate the count of occurrences
    count = last_index - first_index + 1 if first_index != -1 and last_index != -1 else 0

    return count


nums = [1, 1, 2, 2, 2, 2, 3]
target = 2

occurrence_count = count_occurrences(nums, target)
print("The number of occurrences of", target, "is", occurrence_count)
