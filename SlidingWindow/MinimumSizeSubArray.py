"""
209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')

        target_sum = 0
        left = 0

        for right in range(len(nums)):
            target_sum += nums[right]
            
            while target_sum >= target:
                min_length = min(right-left+1,min_length)
                target_sum -= nums[left]
                left += 1
        
        return 0 if min_length == float('inf') else min_length
        
