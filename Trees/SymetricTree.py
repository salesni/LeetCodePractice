"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(root1,root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            
            if root1.val != root2.val:
                return False

            return is_mirror(root1.left,root2.right) and is_mirror(root1.right, root2.left)
        
        return is_mirror(root,root)
            
            

        
