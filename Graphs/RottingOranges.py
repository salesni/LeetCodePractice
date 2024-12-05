"""
994. Rotting Oranges
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,columns = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0,1,2

        #QUE Will register rotten, as it will be the reference like VISITED
        queue = deque()
        num_fresh = 0
        for row in range(rows):
            for col in range(columns):
                cell = grid[row][col]
                if cell == FRESH:
                    num_fresh += 1
                elif cell == ROTTEN:
                    queue.append((row,col))
        if num_fresh == 0:
            return 0
        min_time = -1
        #BFS
        while queue:
            #Level Size as rotten passes per leven and not one by one
            level_size = len(queue)
            min_time += 1
            for _ in range(level_size):
                x,y = queue.popleft()
                for row,col in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0 <= row < rows and 0<=col<columns and grid[row][col] == FRESH:
                        grid[row][col] = ROTTEN
                        num_fresh -= 1
                        queue.append((row,col))

        return min_time if num_fresh == 0 else -1

