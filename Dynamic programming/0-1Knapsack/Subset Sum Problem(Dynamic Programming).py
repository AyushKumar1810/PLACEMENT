#Question :Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# Example:

# Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.

#NOTE: In that we have To make a subsets that will give t sum equal to target sum .. (It can be countinuous or not )
#NOTE to myself : We have to decrease the number of elements by 1 in both Inclusion and exclusion!   Inclusion means, we take current element and start to identify the possible solutions for the remaining sum with rest of the elements!
# Exclusion means, we discard the current element and start to identify the possible solutions for the same sum with rest of the elements excluding the current one!#