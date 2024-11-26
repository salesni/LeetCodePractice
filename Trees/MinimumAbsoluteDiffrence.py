"""
530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between 
the values of any two different nodes in the tree.

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.minimum = float('inf')
        self.prev = None

        def dfs(root: Optional[TreeNode]):

            if root == None:
                return
            
            dfs(root.left)

            if self.prev != None:
                self.minimum = min(self.minimum, abs(self.prev.val-root.val))
            
            self.prev = root

            dfs(root.right)
        
        dfs(root)
        return self.minimum
