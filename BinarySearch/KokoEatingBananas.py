"""
75. Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of 
bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of 
them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

from math import ceil


"""
Example:  [3,6,7,11]
has a possibility of k [1-11]
 the possible ks that solve are
  0.      1.    2.   3.    4.    5.     6     7.   8.    9.    10.   11
 [False,False,False,True, True, True, True, True, True, True, True, True ]

 binary search to find when the false turns to True

"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def does_k_work(piles: List[int], k: int, h: int) -> bool:
            for pile in piles:
                h -= ceil(pile/k)
                if h < 0:
                    return False 
            return True
        
        left = 1
        right = max(piles)
        mid = 0

        while left < right:
            mid = left + (right-left)//2

            if does_k_work(piles,mid,h):
                right = mid
            else:
                left = mid + 1
        return right



        
