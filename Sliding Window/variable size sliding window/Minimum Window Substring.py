#Question:
# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
#NOTE-A very Good question , our 1st Job is to traverse the "T string" and then store it into A HashMap along with it's count . then we will Go to "S string" and comapre it's j value with hash map , if value matches then we will decreament the count value of hashmap character and if it's 0 then we will remove it from HashMap and also we will decrease Hashmap size , we will go untill size of HashMap is 0 ..



def minWindow(s, t):
    # Initialize a dictionary to store the count of characters in t
    charCount = {} # Hashmap
    for ch in t: #Traversing "T"
        if ch in charCount:
            charCount[ch] += 1
        else:
            charCount[ch] = 1

    # Initialize variables to track the minimum window substring
    minLen = float('inf')  # Initially set to infinity
    start = 0  # Starting index of the minimum window substring
    i = 0  # Left pointer of the sliding window
    j = 0  # Right pointer of the sliding window
    count = len(charCount)  # Number of distinct characters in t

    while j < len(s):
        # Update the count of characters in the window
        if s[j] in charCount:
            charCount[s[j]] -= 1
            if charCount[s[j]] >= 0:
                count -= 1

        # Check if all characters in t are present in the window
        if count == 0:
            # Try to minimize the window by moving the left pointer
            while count == 0:
                # Update the minimum window substring if a smaller length is found
                if s[i] in charCount:
                    charCount[s[i]] += 1
                    if charCount[s[i]] > 0:
                        count += 1
                        if j - i + 1 < minLen: # If size of window is less than minlen
                            minLen = j - i + 1
                            start = i
                i += 1

        j += 1

    # Return the minimum window substring
    if minLen == float('inf'):
        return ""
    return s[start: start + minLen]

# Example usage:
s = input("Enter the string: ")
t = input("Enter the target substring: ")
print("Minimum window substring:", minWindow(s, t))
