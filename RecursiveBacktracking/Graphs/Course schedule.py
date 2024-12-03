"""
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 


"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])

        visited = set()
        def dfs(node,visiting):
            if node in visited: return True
            if node in visiting: return False
            visiting.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor,visiting):
                    return False
            visited.add(node)
            return True
        
        for node in list(graph.keys()):
            visiting = set()
            if not dfs(node,visiting):
                return False
        
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])

        #using one Array 
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        node_state = [UNVISITED]*(numCourses+1)

        def dfs(node):
            if node_state[node] == VISITED: return True
            if node_state[node] == VISITING: return False

            node_state[node] = VISITING

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            node_state[node] = VISITED

            return True
        
        for node in list(graph.keys()):
            if not dfs(node):
                return False
        
        return True

    
