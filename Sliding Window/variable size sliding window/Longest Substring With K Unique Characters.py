#Question :Given a string you need to print the size of the longest possible substring that has exactly k unique characters.


# Example:
# Input:
# 2
# aabacbebebe
# 3
# aaaa
# 1
# Output:
# 7
# 4 . 

# In that question we have to find largest subarray of given k unique character

#NOTE- As we have to know two things 1. No of unique and it's count , so we can store it into set and we will get only unique element but we need to find it's count also , " As we know that for finding count the best data structure is Hash map" we will use hash map and in that we will srore arr[j] and it's count also .count will give us the maximum window size and arr[j] will give unique character length and we will comapare it wit given k .. arr[j] will be store in Hash map..

#NOTE-:Approach:
# 1.	Keep on building the substring from j=0 [increasing the window size] and log occurance of each character in a Map.
# 2.	If map size (Unique Characters in Map) becomes greater than k, keep on reducing window size (increase i pointer) and decrease the occurance of character from Map till map size becomes <=k. 
# 3.	If map size becomes equal to k, compute the Candidate answer.
# 4.	Increase j pointer and perform steps 1-3 until j<array size [while loop condition] .

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
s = "aabacbebebe"
k = 3
output=longestkSubstr(s,k)
print(output)