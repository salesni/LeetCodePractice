"""
945. Minimum Increment to Make Array Unique
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.
"""

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        moves=0

        for index in range(len(nums)-1):
            if nums[index] >= nums[index+1]:
                prev_after = nums[index+1]
                nums[index+1] = prev_after + abs(nums[index] - nums[index+1]) + 1
                moves += abs(prev_after - nums[index+1])
        return moves
        
