"""
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])

        def dfs(row,col):

            if row < 0 or row >= rows or col < 0 or col >= columns or grid[row][col] != '1':
                return
            #Mark as visited
            grid[row][col] = '.'
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
        
        num_islands = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    #Not Visited island, mark all its neighbor nodes
                    dfs(row,column)
                    num_islands += 1
        return num_islands




        
