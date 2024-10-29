"""
https://leetcode.com/problems/spiral-matrix/description/
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows, columns = len(matrix), len(matrix[0])
        answer = []
        route_index = 0

        while len(answer) < rows*columns:
            #Top List
            for i in range(route_index, columns - route_index):
                answer.append(matrix[route_index][i])
            
            #Right Column
            for i in range(route_index + 1, rows - route_index):
                answer.append(matrix[i][ columns - route_index-1])
            
            #Bottom Row
            if route_index < (rows - route_index - 1):
                for i in range(columns - route_index - 2, route_index - 1,-1):
                    answer.append(matrix[rows - route_index - 1][i])
            

            #left column
            if route_index < (columns - route_index - 1):
                for i in range(rows - route_index-2, route_index ,-1):
                    answer.append(matrix[i][route_index])

            route_index += 1
        return answer
