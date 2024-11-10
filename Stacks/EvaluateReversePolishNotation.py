"""
150. Evaluate Reverse Polish Notation
Solved
Medium

Topics
Companies
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_digits = deque()
        operator_set = {'+','-','/','*'}

        def operate(num1,num2,oper):
            if oper == '+':
                return num1 + num2
            elif oper == '-':
                return num1 - num2
            elif oper == '*':
                return int(num1 * num2)
            elif oper == '/':
                return int(num1 / num2)
        
        for token in tokens:
            if token not in operator_set:
                stack_digits.append(int(token))
            else:
                num2 = stack_digits.pop()
                num1 = stack_digits.pop()
                stack_digits.append(operate(num1,num2,token))
        return stack_digits.pop()
