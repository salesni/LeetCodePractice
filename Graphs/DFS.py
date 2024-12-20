"""
1971. Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        # def dfs(start,target):

        #     if start == destination: 
        #         return True
        #     visited.add(start)
            
        #     for neighbor in graph[start]:
        #         if neighbor not in visited:
        #             if dfs(neighbor,target):
        #                 return True
        #     return False

                # Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use a stack for iterative DFS
        stack = [source]
        visited = set()

        while stack:
            node = stack.pop()
            if node == destination:
                return True 

            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return False
            
        

