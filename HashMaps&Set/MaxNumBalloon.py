
"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_dict = Counter(text)
        balloon = "balloon"
        
        for key in balloon:
            if key not in char_dict:
                return 0
        
        return min(char_dict["b"],char_dict["a"],char_dict["l"]//2,
                    char_dict["o"]//2, char_dict["n"])
        

"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_dict = defaultdict(lambda: 0)
        balloon = "balloon"

        for char in text:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        for key in balloon:
            if key not in char_dict:
                return 0
        
        return min(char_dict["b"],char_dict["a"],char_dict["l"]//2,
                    char_dict["o"]//2, char_dict["n"])

"""
