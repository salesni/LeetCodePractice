"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False

        s1_counter = [0]*26
        window_counter = [0]*26

        for char in s1:
            s1_counter[ord(char)-ord('a')] += 1
        
        for index in range(len(s1)):
            window_counter[ord(s2[index])-ord('a')] += 1
        
        if s1_counter == window_counter:
            return True
        
        
        for index in range(len(s1),len(s2)):
            #delete previous start from the window
            window_counter[ord(s2[index-len(s1)]) - ord('a')] -= 1
            #Fill with the new end of the window
            window_counter[ord(s2[index]) - ord('a')] += 1

            if s1_counter == window_counter:
                return True
        return False


        
