# Given an array Arr of N positive integers and another number X. Determine whether or not there exist two elements in Arr whose sum is exactly X.

# Example 1:

# Input:
# N = 6, X = 16
# Arr[] = {1, 4, 45, 6, 10, 8}
# Output: Yes
# Explanation: Arr[3] + Arr[4] = 6 + 10 = 16
# Example 2:

# Input:
# N = 5, X = 10
# Arr[] = {1, 2, 4, 3, 6}
# Output: Yes
# Explanation: Arr[2] + Arr[4] = 4 + 6 = 10
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function hasArrayTwoCandidates() which takes the array of integers arr, n and x as parameters and returns a boolean denoting the answer.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

#NOTE: That Below Approach is Brute Force Approach , so we need optimised one 
#NOTE: Time complexivity is O(n^2)
def hasArrayTwoCandidates(arr, n, x):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j]==x:
                return True
    return False
arr1 = [1, 4, 45, 6, 10, 8]
n1 = 6
x1 = 16
print(hasArrayTwoCandidates(arr1, n1, x1)) 
arr2 = [1, 2, 4, 3, 6]
n2 = 5
x2 = 10
print(hasArrayTwoCandidates(arr2, n2, x2)) 

#NOTE: For optimised we will use hashset to store visisting set and put into hashset if not visisted ..
#Our Approach  will be quite very easy we will store each element in hashset and we will take "sum-arr[i]" value , if that value present in hashset then we got it's sum pair if not then we will return false and if we are not visisted the number we will simply add to hashset .

#NOTE: Time complexivity will be O(N)
def hasArrayTwoCandidates(arr, n, x):
    hashset=set()
    for i in range(n):
        if x-arr[i] in hashset:
            return True
        hashset.add(arr[i])
    return False
arr1 = [1, 4, 45, 6, 10, 8]
n1 = 6
x1 = 16
print(hasArrayTwoCandidates(arr1, n1, x1)) 
arr2 = [1, 2, 4, 3, 6]
n2 = 5
x2 = 10
print(hasArrayTwoCandidates(arr2, n2, x2)) 