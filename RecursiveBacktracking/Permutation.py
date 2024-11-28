"""
6. Permutations
Given an array nums of distinct integers, return all the possible
permutations
. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(current:List):

            if len(current) == len(nums):
                ans.append(current[:])
                return
            #Iterate over all numbers 
            for num in nums:
                #If we are missing one it is another permutation
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()
        backtrack([])
        return ans
        
