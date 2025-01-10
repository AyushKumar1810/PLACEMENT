
# Partition a Set into Two Subsets of Equal Sum

# Given an array arr[], the task is to check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

# Examples: 

#     Input: arr[] = [1, 5, 11, 5]
#     Output: True 
#     Explanation: The array can be partitioned as [1, 5, 5] and [11]

#     Input: arr[] = [1, 5, 3]
#     Output: False 
#     Explanation: The array cannot be partitioned into equal sum sets.

def can_partition(arr):
    total_sum = sum(arr)
    
    # If the total sum is odd, it cannot be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    # We need to find a subset with sum equal to half of the total sum
    subset_sum = total_sum // 2
    n = len(arr)
    
    # Initialize DP matrix
    t = [[False for _ in range(subset_sum + 1)] for _ in range(n + 1)]
    
    # Initialization
    for i in range(n + 1):
        t[i][0] = True  # A subset with sum 0 is always possible (empty subset)
    
    # Build the matrix in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, subset_sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    
    return t[n][subset_sum]

def new_func(__name__, can_partition):
    if __name__ == "__main__":
        # Take input from the user
        arr = list(map(int, input("Enter the elements of the array: ").split()))
        
        # Call the can_partition function with the input array
        if can_partition(arr):
            print("True")
        else:
            print("False")

# Call the new_func to execute the code
new_func(__name__, can_partition)


#Pracrice:
def can_Practice(arr,n):
    total_sums = sum(arr)
    if total_sums %2 !=0:
        return False
    subsets_Sum = total_sums //2
   
    t = [[False for _ in range(subsets_Sum + 1)] for _ in range(n + 1)]
    for i in range(n+1):
        t[i][0] = True
    for i in range(1,n+1):
        for j in range(1,subsets_Sum+1):
            if arr[i-1] <=j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][subsets_Sum]
