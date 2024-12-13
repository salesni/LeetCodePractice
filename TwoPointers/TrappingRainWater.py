"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        max_left = 0 
        max_right = 0
        left, right = 0, n -1
        water = 0

        while left <= right:
            if height[left] <= height[right]:
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1

        return water


class Solution:
    def trap(self, height: List[int]) -> int:

        # we need to look
        # for the highest right and left wall, to identify how many
        # water can it store
        length = len(height)
        left_max_walls = [0]*length
        right_max_walls = [0]*length
        max_wall_right = 0
        max_wall_left = 0

        for left, wall in enumerate(height):
            right = length - left -1
            left_max_walls[left] = max_wall_left
            right_max_walls[right] = max_wall_right

            max_wall_left = max(wall, max_wall_left)
            max_wall_right = max(height[right], max_wall_right)
        
        water_count = 0
        for index,wall in enumerate(height):
            potential_water = min(left_max_walls[index], right_max_walls[index])
            water_count += max(0,(potential_water - wall))
        
        return water_count




        
