"""
215. Kth Largest Element in an Array
Solved
Medium

Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
"""
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        for index in range(len(nums)):
            nums[index] *=  -1
        
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
        
        return - heapq.heappop(nums)
      #o(n + k log(n))
      # Space = O(1)

    def findKthLargest(self, nums: List[int], k: int) -> int:

        k_min_heap = []

        for num in nums:
            if len(k_min_heap) < k:
                heapq.heappush(k_min_heap,num)
            else:
                heapq.heappushpop(k_min_heap,num)
        
        return heapq.heappop(k_min_heap)
        # O( nlog(k))
        # Space : O(k)
