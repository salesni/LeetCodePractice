"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_dict = Counter(magazine)
        
        for char in ransomNote:
            if char not in letters_dict:
                return False
            else:
                if letters_dict[char] > 0:
                    letters_dict[char] -= 1
                else:
                    return False
        return True
