## Question - 
# Consider an array of distinct numbers sorted in increasing order. 
# The array has been rotated (Clockwise) k number of times. Given such an array, 
# find the value of k.

# Examples:

# Input : arr[] = {15, 18, 2, 3, 6, 12} ""15 wil go to the last then after 18 will go last"" 
# Output: 2
# Explanation : Initial array must be {2, 3,
# 6, 12, 15, 18}. We get the given array after 
# rotating the initial array twice.

# Input : arr[] = {7, 9, 11, 12, 5}
# Output: 4

# Input: arr[] = {7, 9, 11, 12, 15};
# Output: 0

##NOTE-Here’s the gist of startgic used:-

# 1.	To find the number of rotations in a rotated sorted array,
# we need to find the index of the minimum element, so this question gets converted to 
# finding the index of the minimum element.
# 2.	We need to mention one exceptional case here, that if the array is properly
# sorted (0 times rotation), then we can return 0 in such cases. Now, the minimum element
# possess a unique property here that it is less than both of its adjacent elements, and 
# that is also quite obvious. So as usual we’ll check the mid element if its less than its
# previous as well as its next element. If it comes out to be like this, then it is surely
# the minimum element, and we’ll return its index. One thing we need to take care about is, 
# suppose my mid is pointing to index=0, then how I’ll reach to its previous element, assuming
# that its previous element will be the last element (since it is also a rotated array),
# then for fetching its previous element, we need to do prev=(mid+n-1)%n, here mid+n-1 will give me n-1 and (n-1%n) will be n-1, which is the index of the last element. Similarly, if my mid is pointing to the last element, then its next element has to be the first element of the array, so for that do next=(mid+1)%n. By doing this, we can avoid out of bound situations.
# 3.	Now, if the mid element doesn’t comes out to be the minimum element, we have to move to either side of the array, to pursue the binary search algorithm. We need to move to that part of the array which consists the minimum element, because that’s what we’re finding. Suppose my array is:- 6, 8, 9, 10, 1, 3 ,4 , then mid=3(which is pointing to 10), this mid is not the minimum element, so my array gets divided into two parts, one is (6,8,9,10) an the other is(10,1,2,3), as you can see one part is sorted and the other one is unsorted, so my minimum element always lies in the unsorted part and this is true for every case. So I’ll be moving to this unsorted part of the array.
# 4.	How can I decide which part is sorted and which is unsorted, then only I can proceed moving to the unsorted part in order to find my minimum element. For that, we need to check whether my first element is smaller than the mid element or not, if arr[0]<=arr[mid], then this first part of the array is sorted, and I need to do start=mid+1, in order to move to the second part which is unsorted. Similarly, I’ll check if arr[mid]<=arr[n-1], then the second part is sorted and first part is unsorted, so do end=mid-1. And then keep on doing this, you’ll definitely reach to the minimum element, because it is pretty sure that the minimum element lies somewhere in the array. Return mid, when the condition for the minimum element is hit.

def findMinRotations(arr):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        # Case 1: Array is already sorted
        if arr[start] <= arr[end]:
            return start

        mid = start + (end - start) // 2
        next_index = (mid + 1) % n # we use modulous because suppose mid is in last position then mid +1 will be invalid using mod will give you 1st value of array .
        prev_index = (mid - 1 + n) % n # here it would be (mid-1)%n but suppose mid is in 0th index so (-1) % n will give error so for that we have added +n i.e (mid-1+n)%n will give last index value . like a circular list .

        # Case 2: Check if mid is the minimum element
        if arr[mid] <= arr[prev_index] and arr[mid] <= arr[next_index]: ##NOTE - very very Important point to be remember "for an any array minimum element will be always less than it's previous index value as well as next index value "" .
            return mid
        # Case 3: Discard the right side
        # as  we are using binary search so we can go either left or right .
        #NOTE= As we are seeing minimum element is seeing only in unsorted part .
        elif arr[start] <= arr[mid]:
            start = mid + 1
        # Case 4: Discard the left side
        elif arr[mid] <= arr[end]:
            end = mid - 1

    return -1  # Invalid input or array not rotated

arr = [4,5,6,7,0,1,2]
min_rotations = findMinRotations(arr)
print("Minimum rotations required:", min_rotations)