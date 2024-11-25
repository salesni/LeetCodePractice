"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trees_equal(self, root1:Optional[TreeNode],root2:Optional[TreeNode]):
            
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            
            if root1.val == root2.val:
                return self.trees_equal(root1.right,root2.right) and self.trees_equal(root1.left,root2.left)
            else:
                return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root == None:
            return False
        if subRoot == None:
            return True
        if root.val == subRoot.val:
            if self.trees_equal(root,subRoot):
                return True
        
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)

        

        
