# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.

def min_remove_to_make_valid(s: str) -> str:
    stack = []
    to_remove = set()
    
    # First pass: Find indices of parentheses to remove
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    
    # Second pass: Remove parentheses marked for removal
    result = []
    for i, char in enumerate(s):
        if i not in to_remove and (not stack or i != stack[-1]):
            result.append(char)
    
    return ''.join(result)
# Test cases
print(min_remove_to_make_valid("lee(t(c)o)de)"))  # Output: "lee(t(c)o)de"
print(min_remove_to_make_valid("a)b(c)d"))        # Output: "ab(c)d"
print(min_remove_to_make_valid("))(("))           # Output: ""