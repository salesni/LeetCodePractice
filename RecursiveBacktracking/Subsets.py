"""
78. Subsets
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current = []
        length = len(nums)

        def backtrack(i):
            if i == length:
                #A copy is sent due to python
                ans.append(current[:])
                return
            #Do not take into consideration nums[i]
            backtrack(i+1)

            current.append(nums[i])
            #Consider num[i]
            backtrack(i+1)

            current.pop()
        
        backtrack(0)
        return ans
