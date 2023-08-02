# QUESTION= Given a sorted array, find the element in the array which has minimum 
# difference with the given number. .
#NOTE- After finishing while loop low<=high(without target/key is present)
#The low pointer points towards right side of target value (we assume ) 
# and high pointer Points towards left side of target value (we assume ).
#for example arr = [1, 3, 8, 10, 15] , key = 12 so as we can see key is not present
# so after finishing while loop ,  our low pointer will be on the top most right 
# i.e at 15 and high will be pointing at 10 

# so the basic idea we are using is that if key is not present , so after 
# finishing our low and high pointer will be just towars left and right side of our
# imaginary target/key value so as our array is sorted so left and right pointer of
# target value difference will be samll and we have to take " absolute (abs)" value
# to avoid negative value

def find_min_difference(arr, key):
    #Binary search
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
# For finding least absolute difference
    value1 = arr[start] - key# start pointer will be at right of our key
    value2 = arr[end] - key#end pointer will be at left of our key
    c1 = abs(value1) # for avaoiding negative value
    c2 = abs(value2)# for avaoiding negative value

    if c1 < c2: # finding minimum value between c1=start and c2=end
        return arr[start]
    else:
        return arr[end]

# Example usage
arr = [1, 3, 8, 10, 15] #[12-1,12,-3,12-8,12-10,15-12]=[1,9,4,2,3]
key = 12
result = find_min_difference(arr, key)
print(result)
