# Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

# Example:

# Input:
# N = 4, K = 2
# Arr = [100, 200, 300, 400]
# Output:
# 700
# Explanation:
# Arr3  + Arr4 =700,
# which is maximum. . 

def max_sub_array():
    array=[2, 3, 4, 6, 5, 1, 4, 2, 3]
    window_size=3
    custom_sum=sum(array[:window_size])
    Max_sum=0
    for i in range(window_size,len(array)):
        new_sum = custom_sum - array[i-window_size] + array[i] # That is the main point here we are susbtracting 1st value of the prevoius sum and adding next value for finding new sum . i.e custom_sum= 9 (2+3+4) but for finding next sum we have to traverse from index 3 to 8th index and we have to substract 0th index value and add 3rd index value then substract 1st index value and then add 4th index value to it . array[i-window_size] Will Give us 1st index of previous sub array.. For next subarray sum= 9 - 2 + 6 = 13
        if new_sum > Max_sum:
            Max_sum=new_sum
        custom_sum=new_sum
    print("Maximun sum is" , Max_sum)
max_sub_array()