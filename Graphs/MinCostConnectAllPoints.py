"""
1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path 
between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        import heapq
        visited = set()
        min_heap = [(0,0)]
        total_cost = 0
        points_len = len(points)

        while len(visited) < points_len:
            distance, start = heapq.heappop(min_heap)

            if start in visited:
                continue

            visited.add(start)
            total_cost += distance
            x_start, y_start = points[start]

            for next_node_index in range(points_len):
                if next_node_index not in visited:
                    x_next, y_next = points[next_node_index]
                    manhattan_distance = abs(x_start - x_next) + abs(y_start - y_next)
                    heapq.heappush(min_heap,(manhattan_distance,next_node_index))
        return total_cost
