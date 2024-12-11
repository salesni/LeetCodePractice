"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. 
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        #ITERATE OVER A TARGET VALUE
        def verify(target:int):
            top_rotations, bottom_rotations = 0,0
            for top, bottom in zip(tops,bottoms):
                if top != target and bottom !=target:
                    return -1
                if top != target:
                    top_rotations += 1
                elif bottom != target:
                    bottom_rotations += 1
            return min(bottom_rotations,top_rotations)
        
        rotations_top = verify(tops[0])

        if rotations_top != -1:
            return rotations_top
        else:
            return verify(bottoms[0])
        
        

        # n = len(tops)
        # num_counter = [0]*6
        # top_counter = [0]*6
        # bottom_counter = [0] * 6

        # for num in tops:
        #     num_counter[num-1] += 1
        #     top_counter[num-1] += 1
        
        # for index, num in enumerate(bottoms):
        #     if tops[index] != num:
        #         num_counter[num-1] += 1
        #     bottom_counter[num-1] += 1
        
        # are_n = False
        # num_repeated = -1
        # for  index, count in enumerate(num_counter):
        #     if count >= n:
        #         are_n = True
        #         num_repeated = index
        
        # if are_n:
        #     return min(max(n-top_counter[num_repeated],0), max(n-bottom_counter[num_repeated],0))
        # else:
        #     return -1

