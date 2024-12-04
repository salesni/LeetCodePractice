"""
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the
island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer 
matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain 
water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

"""

from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,columns = len(heights), len(heights[0])
        pacific_ocean_path = set()
        pacific_queue = deque()
        atlantic_ocean_path = set()
        atlantic_queue = deque()

        #Fill default  vslues Pacific Ocean
        for col in range(columns):
            pacific_ocean_path.add((0,col))
            pacific_queue.append((0,col))
        
        for row in range(rows):
            pacific_ocean_path.add((row,0))
            pacific_queue.append((row,0))
        #Fill for Atlantic Ocean
        for col in range(columns):
            atlantic_ocean_path.add((rows-1,col))
            atlantic_queue.append((rows-1,col))
        
        for row in range(rows):
            atlantic_ocean_path.add((row,columns-1))
            atlantic_queue.append((row,columns-1))
        
        def bfs(queue, visited):
            while queue:
                node = queue.popleft()
                x,y = node[0],node[1]
                for row,col in [(x-1,y),(x+1,y), (x,y-1), (x,y+1)]:
                    if 0<= row < rows and 0 <= col < columns  and (row,col) not in visited \
                        and heights[row][col] >= heights[x][y] :
                        queue.append((row,col))
                        visited.add((row,col))
        
        bfs(pacific_queue,pacific_ocean_path)
        bfs(atlantic_queue,atlantic_ocean_path)

        result = list( pacific_ocean_path & atlantic_ocean_path )
        return result

        



        
        
