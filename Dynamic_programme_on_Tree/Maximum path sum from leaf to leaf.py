#question - 
# If a binary tree is given, how to find Maximum path sum between two leaves of binary tree.

# All should be numbers
# The maximum sum path may or may not go through root.
# For example, in the following binary tree, the maximum sum is 27(3 + 6 + 9 + 0 – 1 + 10). Expected time complexity is O(n).

#   -15
#  /  \
# 5    6
# / \  / \
# -8 1 3  9
# / \       \ 
# 2  6       0
# / \
# 4  -1
# /
#10

def solve(root, res):
    if root is None:
        return 0
    
    l = solve(root.left, res)
    r = solve(root.right, res)
    
    temp = max(max(l, r) + root.val, root.val)
    ans = max(temp, l + r + root.val)
    res = max(res, ans)
    
    return temp

class Solution:
    def maxPathSum(self, root):
        res = float('-inf')
        solve(root, res)
        return res
