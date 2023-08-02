#Question - Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

#NOTE-Key thing : diameter at each node is defined by 1 + lh (height of left tree) + rh (height of right tree) {i.e height of right subtree + height of left subtree + 1 } . Just calculate that at each node to get the maximum diameter.
# Hence use the height method for binary tree and just add the line to calculate the diameter which gives the O(N) solution.

diameter = float('-inf')

def getDiameter(root):
    global diameter
    # Base case: If the node is None, return 0 as it represents an empty subtree
    if root is None:
        return 0
    
    # Recursively calculate the heights of the left and right subtrees
    left = getDiameter(root.left) # calculating left height
    right = getDiameter(root.right) # calculating right height
    
    # Calculate the diameter passing through the current node
    temp = max(left , right ) +1  #  passing through root node then it would only be so either the path will be starting from right node or left depending upon who has max value and just add 1 for the root node height
    
    # Update the global diameter variable if the diameter at the current node is greater
    diameter = max(temp , left + right + 1) # If  not passing through root node then , it would be just either max of temp or left + right + 1
    
   
    return temp 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calculate the diameter
result = getDiameter(root)
print("Diameter:", result)

