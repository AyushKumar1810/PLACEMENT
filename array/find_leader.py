# Leaders in an Array
# Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

# Examples
# Example 1:
# Input:
#  arr = [4, 7, 1, 0]
# Output:
#  7 1 0
# Explanation:
#  Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

# Example 2:
# Input:
#  arr = [10, 22, 12, 3, 0, 6]
# Output:
#  22 12 6
# Explanation:
#  6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.

#NOTE: we will start from last as we will know that last element is always a leader so will append last element to result and we will decreament 1 by 1 so we will now move to 2nd last and we will check it with last element that if it's greater than last element or no if it's then we will decide it;s leder or not ..

def printLeaders(arr , n):
    ans=[]
  # Last element of an array is always a leader,
    # push into ans array.
    max_elem=arr[n-1]
    ans.append(arr[n-1])
 # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range (n-2,-1,-1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem=arr[i]
    return ans
# Main function

if __name__ == '__main__':
    # Array Initialization
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeaders(arr, n)

    for i in range(len(ans)-1, -1, -1):
        print(ans[i], end=" ")

    print()