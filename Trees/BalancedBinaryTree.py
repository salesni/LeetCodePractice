"""
110. Balanced Binary Tree
Solved
Easy

Topics
Companies
Given a binary tree, determine if it is 
height-balanced
.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> Tuple[int,bool]:
        
        if root == None:
            return 0, True
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if not left[1] or not right[1]:
            return 0, False

        is_balanced = abs(left[0]-right[0])<=1

        return 1 + max(left[0],right[0]), is_balanced
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.maxDepth(root)[1]
