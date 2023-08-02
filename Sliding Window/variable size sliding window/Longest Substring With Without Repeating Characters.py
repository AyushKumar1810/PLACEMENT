#Question ::Given a string s, find the length of the longest substring without repeating characters.


# Example:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring

#NOTE- here evething is same as previous question but difference is that we want withoutteapaeating character and also it's Not given K size so we don't know to which we have to compare our condition . so we will compare it with window size ,we can solve this problem using hash map or with set ..

def lengthOfLongestSubstring(s) -> int:
    if len(s) == 0:
        return 0

    charMap = {}  # Dictionary to store character counts
    i = j = 0  # Pointers for start and end of the substring
    n = len(s)  # Length of the input string
    mx = float('-inf')  # Maximum length of substring

    while j < n:
            # Increment the count of current character in the dictionary
        ch = s[j]  # Current character ( we are storing each value in ch)

        # Update the character frequency in the charMap
        if ch in charMap: # if we found ch already in hashmap
            charMap[ch] += 1 # increase the count of that character
        else:
            charMap[ch] = 1

            # If the current substring has all unique characters
        if len(charMap) == j - i + 1: # here instead of given k value we are comparairing our conditions with window size as max unique character will be equal to size of window
            mx = max(mx, j - i + 1)  # Update the maximum length
            j += 1  # Move the end pointer to the next position

            # If the current substring has duplicate characters
        elif len(charMap) < j - i + 1:
            while len(charMap) < j - i + 1:
                    # Decrement the count of characters from the start of the substring
                charMap[s[i]] -= 1
                    # If the count becomes 0, remove the character from the dictionary
                if charMap[s[i]] == 0:
                    del charMap[s[i]]
                i += 1  # Move the start pointer to the next position

            j += 1  # Move the end pointer to the next position

    return mx  # Return the maximum length of the substring
s = "pwwkew"
print(lengthOfLongestSubstring(s))