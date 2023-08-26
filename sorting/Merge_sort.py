# #Intuition: 

# Merge Sort is a divide and conquers algorithm, it divides the given array into equal parts and then merges the 2 sorted parts. 
# There are 2 main functions :
# merge(): This function is used to merge the 2 halves of the array. It assumes that both parts of the array are sorted and merges both of them.
# mergeSort(): This function divides the array into 2 parts. low to mid and mid+1 to high where,
#  low = leftmost index of the array
#  high = rightmost index of the array
#  mid = Middle index of the array 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Split the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursive call on the left half
        merge_sort(right_half)  # Recursive call on the right half

        i = j = k = 0

        # Merge the two halves while comparing elements
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr)
