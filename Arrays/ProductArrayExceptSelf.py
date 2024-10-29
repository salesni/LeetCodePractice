"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        overall_mult:int = 1

        zero_flag = False
        zero_counter = 0

        for num in nums:
            if num != 0:
                overall_mult *= num
            else:
                zero_flag = True
                zero_counter +=1
        
        new_arr = []

        for num in nums:
            if zero_counter > 1:
                new_arr.append(0)
            else:
                if num == 0:
                    new_arr.append(overall_mult)
                elif zero_flag:
                    new_arr.append(0)
                else:
                    new_arr.append(int(overall_mult/num))
        return new_arr
