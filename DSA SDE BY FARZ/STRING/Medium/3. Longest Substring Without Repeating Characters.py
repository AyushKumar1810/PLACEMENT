# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

#Brute Force Approach:
# Initialize a variable to keep track of the maximum length of the substring without repeating characters.
# Iterate through each character in the string.
# For each character, start a new substring from that character and keep adding characters to it until you encounter a repeating character.
# Update the maximum length if the current substring length is greater than the maximum length found so far.
# Repeat this process for all characters in the string.
# Return the maximum length found.

def length_of_longest_substring(s: str) -> int:
    max_length=0
    for i in range(len(s)):
        seen=set()
        length=0
        for j in range(i,len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                length+=1
                max_length=max(max_length,length)
            else:
                break
    return max_length
s = "pwwkew"
print(length_of_longest_substring(s))

# Optimized Approach:
# Initialize two pointers, start and end, to keep track of the current substring without repeating characters.
# Use a dictionary to store the index of the last occurrence of each character.
# Iterate through the string and update the start pointer to the maximum of its current value and the index of the last occurrence of the current character plus one.
# Update the maximum length by subtracting start from the current index plus one.
# Update the last occurrence index of the current character in the dictionary.
# Repeat this process for all characters in the string.
# Return the maximum length found.

def length_of_longest_substring(s: str) -> int:
    max_length = 0
    last_occurrence = {}
    start = 0
    for end in range(len(s)):
        if s[end] in last_occurrence:
            start = max(start, last_occurrence[s[end]] + 1)
        max_length = max(max_length, end - start + 1)
        last_occurrence[s[end]] = end
    return max_length
s = "abcabcbb"
print(length_of_longest_substring(s))