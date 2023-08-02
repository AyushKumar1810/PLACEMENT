#Question - Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# NOTE- the question is same as diameter difference is only we have to calculate the value by taking sum of each .. 

def maxpathsum(root):
    res=float("-inf")
    def dp(root):
        nonlocal res 
        if not root :
            return 0
        left_sum=dp(root.left)
        right_sum=dp(root.right)
        temp=max(max(left_sum , right_sum ) + root.val , root.val)
        ans=max(temp,left_sum + right_sum + root.val)
        res=max(res,ans)
        return temp
    return res
