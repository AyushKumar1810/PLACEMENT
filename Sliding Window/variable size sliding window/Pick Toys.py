#Question ::
# Problem Description: No Where, it was an interview problem

# John is at a toy store help him pick maximum number of toys. He can only select in a continuous manner and he can select only two types of toys.


# Example:
# Input:
# 1
# abaccab

#NOTE- we have two very important conditions :
#1.john have to buy toy in countineous manner that means we will get subarray or substring of original , and it will be of contigious manner 
#2.he can only choose two (2) types of toy that means maximum unique element will be 2 ..
 #After seeing two condition we are getting that this question is same as " Longest substring with k unique character " 


def longestkSubstr(s, k):
    charMap = {}  # Dictionary to store character frequency
    i = 0  # Window start index
    j = 0  # Window end index
    maxStringLen = -1  # Maximum length of substring with at most k distinct characters

    while j < len(s):
        ch = s[j]  # Current character ( we are storing each value in ch)

        # Update the character frequency in the charMap
        if ch in charMap: # if we found ch already in hashmap
            charMap[ch] += 1 # increase the count of that character
        else:
            charMap[ch] = 1 # Otherwise reamins 1

        if len(charMap) < k:
            # If the number of distinct characters is less than k, expand the window
            j += 1
        elif len(charMap) == k:
            # If the number of distinct characters is equal to k, update the maxStringLen and expand the window
            maxStringLen = max(maxStringLen, j - i + 1) # for finding length j-i+1 
            j += 1
        elif len(charMap) > k:
            # If the number of distinct characters is greater than k, shrink the window from the left
            while len(charMap) > k and i < len(s):
                # Remove the character at the window start index and update the frequency in charMap
                charMap[s[i]] -= 1 # we will decrease the window size and will remove arr[i] value 
                if charMap[s[i]] == 0: # for removing we have to make it's count 0 
                    del charMap[s[i]] # after that we are removing it 
                i += 1 # after removing we will increament i value for getting unique value
            j += 1

    return maxStringLen
s = "abaccab"
k = 2
output=longestkSubstr(s,k)
print(output)

