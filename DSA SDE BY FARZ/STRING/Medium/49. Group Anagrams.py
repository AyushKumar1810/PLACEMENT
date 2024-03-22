# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# # strs[i] consists of lowercase English letters.

from collections import defaultdict

def group_anagrams(strs):
    anagrams_dict = defaultdict(list)

    for s in strs:
        sorted_s = "".join(sorted(s))
        anagrams_dict[sorted_s].append(s)

    return list(anagrams_dict.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
