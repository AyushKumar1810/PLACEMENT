# Given an ""array of letters sorted in ascending order"", find the smallest letter in the the array which is greater than a given key letter.

# the problem is same as "Ceil problem " which is for integer but now we have alphabet ....
##NOTE = This problem is difference from "ceil problem " In two ways >>>
# *> Here instead of integer it's character so we will return char
# **>> Here "if key == arr[mid]:" then we are  doing this - "return arr[mid]" In last problem But in this we have to find greater if it's equal to or not ..



def next_greatest_letter(letters, target):
    n = len(letters)
    start = 0
    end = n - 1
    res = letters[0]
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if target == letters[mid]:
            start = mid + 1
        elif target < letters[mid]:
            res = letters[mid]
            end = mid - 1
        elif target > letters[mid]:
            start = mid + 1

    return res
letters = ['a', 'c', 'f', 'h']
target = 'c'
result = next_greatest_letter(letters, target)
print("Next greatest letter:", result)



