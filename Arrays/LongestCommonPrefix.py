"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        base_string = strs[0]
        for string in strs:
            min_length = min(len(string),min_length)

        index = 0
        while index < min_length:
            for string in strs:
                if base_string[index] != string[index]:
                    return base_string[:index]
            index += 1
        return base_string[:index]
