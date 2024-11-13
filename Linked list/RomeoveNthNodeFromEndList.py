"""
19. Remove Nth Node From End of List
Solved
Medium

Topics
Companies

Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        target = length - n
        current = dummy
        counter = 0

        # Second pass to find the node just before the target
        while counter < target:
            current = current.next
            counter += 1

        current.next = current.next.next

        return dummy.next
