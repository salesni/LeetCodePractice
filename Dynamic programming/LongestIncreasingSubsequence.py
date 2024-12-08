"""
300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        DP = [1] * len(nums)

        for lock_index in range(1,len(nums)):
            lock = nums[lock_index]
            for num_index in range(lock_index):
                num = nums[num_index]
                if num < lock:
                    DP[lock_index] = max(DP[lock_index], 1 + DP[num_index])

        return max(DP)

        

