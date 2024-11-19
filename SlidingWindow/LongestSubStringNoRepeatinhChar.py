"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.
 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sub_str_set = set()
        sub_str_start = 0
        max_length = 0

        for index, char in enumerate(s):

            if char not in sub_str_set:
                sub_str_set.add(char)
            else:
                max_length = max(max_length, len(sub_str_set))
                while char  in sub_str_set:
                    sub_str_set.remove(s[sub_str_start])
                    sub_str_start += 1
                sub_str_set.add(char)
        max_length = max(max_length, len(sub_str_set))
        return max_length


            
        
