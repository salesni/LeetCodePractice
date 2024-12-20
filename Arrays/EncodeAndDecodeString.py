"""
Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length= len(string)
            encoded += f"{length}#{string}"
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        length = len(s)
        index = 0
        ans = []
        while index < length:
            num_index = index 
            while s[num_index] != "#":
                num_index += 1
            str_len = int(s[index:num_index])
            ans.append(s[num_index+1:num_index+1+str_len])
            index = num_index+1+str_len
        return ans


