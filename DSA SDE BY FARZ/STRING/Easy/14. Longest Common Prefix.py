# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


#NOTE:Certainly! Let's illustrate the function longestCommonPrefix with an example:

# Consider the input strs = ["flower", "flow", "flight"].

# Initialize prefix to be the first string in the list: "flower".
# Start iterating from the second string "flow".
# Check if "flow" starts with the current prefix. Since it does, move to the next string.
# Next, check if "flight" starts with the current prefix. Since it also does, move to the next string.
# After iterating through all strings, the prefix remains "fl", which is the longest common prefix among all strings.
# Return "fl" as the output.
# So, for the input ["flower", "flow", "flight"], the output of the function will be "fl".
def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example usage:
strs1 = ["flower","flow","flight"]
print("Output for strs1:", longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog","racecar","car"]
print("Output for strs2:", longestCommonPrefix(strs2))  # Output: ""
