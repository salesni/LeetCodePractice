"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])

        def backtrack(row,col,target_index):
            if target_index == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if board[row][col] == word[target_index]:
                #marked as visited to avoid repeating loots
                temp = board[row][col] 
                board[row][col] = "."
                left = backtrack(row-1,col,target_index + 1)
                right = backtrack(row+1,col,target_index + 1)
                top = backtrack(row,col-1,target_index + 1)
                bottom = backtrack(row,col+1,target_index + 1)
                result = left or right or top or bottom
                board[row][col] = temp
                return result
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row,col,0):
                    return True
        
        return False

        # Time: o(m*k * 4^k)
        

                
        
