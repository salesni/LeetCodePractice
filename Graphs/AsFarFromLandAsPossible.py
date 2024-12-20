"""
1162. As Far from Land as Possible

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents
land, find a water cell such that its distance to the nearest land cell is maximized, and return
the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) 
and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

"""

from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row,col))

        #Perform Multi BFS
        if len(queue) == n**2 or len(queue) == 0:
            return -1
        
        result = -1
        while queue:
            level_size = len(queue)
            result += 1
            for _ in range(level_size):
                row,col = queue.popleft()
                diffs = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]

                for newRow, newCol in diffs:
                    if min(newRow,newCol) < 0 or max(newRow,newCol) >= n:
                        continue
                    if grid[newRow][newCol] == 0:
                        grid[newRow][newCol] = 1
                        queue.append((newRow,newCol))
        return result 
