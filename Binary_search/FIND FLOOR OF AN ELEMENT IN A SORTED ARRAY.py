# Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x. Write efficient functions to find floor of x.

# Example:

# Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
# Output : 2
# 2 is the largest element in arr[] smaller than 5


##NOTE= The idea we are using is that when our mid is less than target element .
# i.e arr[mid] < target , then definetly mid will be a countender for floor of x as it will less than target element and we updated into a temeprory variable res . 

# In short we have to find just less value than our target value ..
def floor(arr,target):
    start =0
    end=len(arr)-1
    res=-1
    while start <= end :
        mid=start + (end - start ) //2
        if target==arr[mid]:
            return arr[mid]
        if arr[mid] < target :
            res=arr[mid] # If we have To return value , if we have to return index then we will write "res=mid"..
            start=mid+1
        elif arr[mid] > target:
            end =mid-1
    return res    
arr = [2, 4, 6, 8, 10, 12]
key = 7
result = floor(arr, key)
print("floor value:", result)
