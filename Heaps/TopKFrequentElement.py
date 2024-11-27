"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter  = Counter(nums)

        min_heap = []

        for key,freq in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq,key))
            else:
                heapq.heappushpop(min_heap,(freq,key))
        
        ans = [item[1] for item in min_heap]

        return ans

     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        length = len(nums)

        buckets = [0] * (length+1)

        for key,freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [key]
            else:
                buckets[freq].append(key)
        
        ans = []
        for index in range(length):
            if buckets[length-index]:
                ans.extend(buckets[length-index])
            if len(ans) == k:
                break
        
        return ans

    

        
