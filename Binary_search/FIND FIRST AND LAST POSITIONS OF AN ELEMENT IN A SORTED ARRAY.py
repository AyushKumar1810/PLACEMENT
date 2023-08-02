#QUESTIONS :
# Given a sorted array with possibly duplicate elements, the task is
# to find indexes of first and last occurrences of an element x in the given array.

# Example:

# Input : arr[] = {1, 3, 5, 5, 5, 5 ,67, 123, 125}    
#         x = 5
# Output : First Occurrence = 2
#          Last Occurrence = 5


##NOTE= So for 1st occurence we can compare with our target element
#  with previous value if it's same then it's not 1st occurance  , 
# if it's not same then it will definetly 1st occurance as array is 
#  in sorted so obivouly some less or greater element will be on it's
#  start . and For last occurance we have to compare it with end side
#  ,if it's same then we move the pointer +1 otherwise it will be last occurance.

def binary_search(nums, target, find_first=True):
    start = 0
    end = len(nums) - 1
    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:# if the target No is mid element then 
            #  we store it into a variable result
            result = mid

            if find_first: # we are checking for 1st occurance for that ,
                #  we have to comapare with the start so end will shift to mid -1 
                end = mid - 1  # Search towards the start
            else: # for last Occurance 
                start = mid + 1  # Search towards the end
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return result

nums = [1, 2, 3, 5, 5, 5, 5, 6, 7, 8, 9]
target = 5

first_occurrence = binary_search(nums, target, find_first=True)
last_occurrence = binary_search(nums, target, find_first=False)

print(first_occurrence)
print(last_occurrence)
