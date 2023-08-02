# In this question we don't know whether our array is
#  sorted in assending order or in descending order .
##NOTE- Binary search can only impliment when our array is in sorted order. 
## Question Name - "ORDER AGNOSTIC SEARCH"

#The main concept we are using is that we have to compare start with end 
# If start<End then it must be of assending order Else it must be descending order . 
def find_ind(arr, target):
    start = 0
    end = len(arr) - 1
    is_ascending = arr[start] < arr[end]

    while start <= end:
        mid = (start + end) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid

        # Determine the next search range based on the target value and the order of the array
        if is_ascending:
            if arr[mid] < target:
                # If the middle element is less than the target, search the end half
                start = mid + 1
            else:
                # If the middle element is greater than the target, search the start half
                end = mid - 1
        else:
            if arr[mid] > target:
                # If the middle element is greater than the target, search the end half
                start = mid + 1
            else:
                # If the middle element is less than the target, search the start half
                end = mid - 1

    # Target value not found
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_ind(arr, 2))

