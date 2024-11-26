"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sort_nodes = []

        def dfs(root:Optional[TreeNode]):
            if root == None:
                return
            
            dfs(root.left)
            sort_nodes.append(root.val)
            dfs(root.right)
        dfs(root)

        if len(sort_nodes) >= k:
            return sort_nodes[k-1]
        else:
            return -1

#use global variables instead of list

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [-1]
        counter =[k]

        def dfs(root:Optional[TreeNode]):
            if root == None:
                return
            
            if counter[0] == 0:
                return
            
            dfs(root.left)

            if counter[0] == 1:
                ans[0] = root.val
            counter[0] -= 1

            if counter[0] > 0:
                dfs(root.right)

        dfs(root)
        return ans[0]


        
