'''
Author:    ZHAO Zinan
Created: 10-Nov-2018

206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        node0 = head
        node1 = head.next
        node2 = node1.next
        head.next = None
        
        while node2:
            node1.next = node0
            node0 = node1
            node1 = node2
            node2 = node2.next
            
        node1.next = node0
        return node1
            