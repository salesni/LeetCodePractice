"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getHeightAndDiameter(self, root: Optional[TreeNode]) -> Tuple[int,int]:
            if root == None:
                return 0,0
            
            left_data = self.getHeightAndDiameter(root.left)
            right_data = self.getHeightAndDiameter(root.right)
            max_diameter = max(left_data[1],right_data[1],left_data[0] + right_data[0])

            return 1 + max(left_data[0],right_data[0]), max_diameter
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getHeightAndDiameter(root)[1]

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def getMaxHeight(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0

            left = getMaxHeight(root.left)
            right = getMaxHeight(root.right)

            max_diameter[0] = max(max_diameter[0], left + right)

            return 1 + max(left,right)
        getMaxHeight(root)
        return max_diameter[0]

