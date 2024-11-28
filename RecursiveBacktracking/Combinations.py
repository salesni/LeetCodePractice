"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(solution:List,start):
            if len(solution) == k:
                ans.append(solution[:])
                return
            # Prunning used to remove unnecesary iterations
            # (k-len(solution))+1
            for i in range(start, n+1 - (k-len(solution))+1):
                solution.append(i)
                backtrack(solution,i+1)
                solution.pop()
        
        backtrack([],1)
        return ans
        
