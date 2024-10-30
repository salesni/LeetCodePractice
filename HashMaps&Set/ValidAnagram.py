"""
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter

"""
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        
        for char in t:
            if char not in s_counter:
                return False
            else:
                if s_counter[char] > 0:
                    s_counter[char] -= 1
                else:
                    return False
        return True

"""
