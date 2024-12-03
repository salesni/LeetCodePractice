"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,columns = len(grid), len(grid[0])
        max_area = 0

        def dfs(row,col) -> int:

            if row < 0 or row >= rows or col < 0 or col >= columns or grid[row][col] != 1:
                return 0
            #visited
            grid[row][col] = 0
            
            left = dfs(row - 1,col)
            right = dfs(row + 1, col) 
            bottom = dfs(row, col + 1)
            top = dfs(row, col - 1)
            return 1 + left + right + top + bottom 

        for row in range(rows):
            for column in range(columns):
                max_area = max(max_area,dfs(row,column))
        return max_area


