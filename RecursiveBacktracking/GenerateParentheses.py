"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(open:int, closed:int, solution:str):
            if len(solution) == 2*n:
                ans.append(solution)
            
            if open < n:
                backtrack(open +1, closed, solution + '(')
            
            if closed < open:
                backtrack(open, closed + 1, solution + ')')
        
        backtrack(0,0,'')
        return ans
        
