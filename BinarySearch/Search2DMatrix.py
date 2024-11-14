"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
""""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search_list(arr:List[int], target:int):

            left, right = 0, len(arr)

            while left <= right:
                mid = left + (right-left)//2

                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            return False
        
        row, col = len(matrix) - 1, len(matrix[0]) - 1

        top, bottom = 0, row

        while top <= bottom:
            mid = top + (bottom-top)//2
            if target >= matrix[mid][0] and target <= matrix[mid][col]:
                return binary_search_list(matrix[mid],target)
            elif target > matrix[mid][col]:
                top = mid +1
            else:
                bottom = mid - 1
        
        return False
        
