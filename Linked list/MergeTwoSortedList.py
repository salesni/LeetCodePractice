"""

21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode()

        current1 = list1
        current2 = list2
        current3 = new_head

        while current1 and current2:
            if current1.val < current2.val:
                current3.next = current1
                current1 = current1.next
            else:
                current3.next = current2
                current2 = current2.next
            current3 = current3.next
        
        current3.next = current1 if current1 else current2
        
        return new_head.next




        
