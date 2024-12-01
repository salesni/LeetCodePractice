"""
16. 3Sum Closest
Solved
Medium

Topics
Companies
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        min_sum = 0
        target_distance_min = float('inf')

        nums.sort()

        for offset in range(len(nums)):

            if offset > 0 and nums[offset] == nums[offset-1]:
                continue
            
            left = offset + 1
            right = len(nums) - 1

            while left < right:
                
                sum_nums = nums[offset] + nums[left] + nums[right]

                if sum_nums == target:
                    return sum_nums

                
                if target_distance_min > abs(sum_nums - target):
                    target_distance_min = abs(sum_nums - target)
                    min_sum = sum_nums
                
                if sum_nums < target:
                    left += 1
                else:
                    right -= 1
        return min_sum
