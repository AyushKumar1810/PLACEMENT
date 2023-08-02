def findMissingAndDuplicates(arr):
    n = len(arr)
    
    # Swap elements to their correct positions
    i = 0
    while i < n:
        if arr[i] != arr[arr[i] - 1]:
            # Swap
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
        else:
            i += 1

    missing_numbers = []
    duplicate_numbers = []

    # Find missing and duplicate numbers
    for i in range(n):
        if arr[i] != i + 1:
            duplicate_numbers.append(arr[i])
            missing_numbers.append(i + 1)

    return missing_numbers, duplicate_numbers

# Example usage:
arr = [3,2,3,4,5,6,7, 1, 2, 5, 3]
missing, duplicates = findMissingAndDuplicates(arr)
print("Duplicate Numbers:", duplicates)
print("Missing Numbers:", missing)
