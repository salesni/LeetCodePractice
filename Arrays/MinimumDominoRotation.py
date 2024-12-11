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

