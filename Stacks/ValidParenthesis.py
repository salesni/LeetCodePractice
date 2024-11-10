"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        open_bracket_stack = deque()
        for char in s:
            if char not in close_brackets:
                open_bracket_stack.append(char)
            else:
                if open_bracket_stack:
                    latest_open_bracket = open_bracket_stack.pop()

                    if latest_open_bracket != close_brackets[char]:
                        return False
                else:
                    return False
        
        return not open_bracket_stack 

            
