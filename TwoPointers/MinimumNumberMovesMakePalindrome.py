"""
2193. Minimum Number of Moves to Make Palindrome

You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Note that the input will be generated such that s can always be converted to a palindrome.

 

Example 1:

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.
Example 2:

Input: s = "letelt"
Output: 2
Explanation:
One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
Other palindromes such as "tleelt" can also be obtained in 2 moves.
It can be shown that it is not possible to obtain a palindrome in less than 2 moves.

"""
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        left, right = 0, len(s)-1
        s = list(s)
        swaps = 0

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                change = right
                while change > left and s[change] != s[left]:
                    change -= 1
                if change == left:
                    #if there is no character equal change left to be closer to the middle
                    s[left],s[left+1] = s[left+1],s[left]
                    swaps += 1
                else:
                    #Make Adjacent Changes
                    for index in range(change,right):
                        s[index],s[index+1] = s[index+1],s[index]
                        swaps+=1
                    left += 1
                    right -= 1
        return swaps
