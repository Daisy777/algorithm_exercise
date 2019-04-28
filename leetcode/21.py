zpython'''
Author: ZHAO Zinan
Created: 26. April 2019

21. Merge Two Sorted Lists
''' 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val > l2.val:
            l2, l1 = l1, l2
            
        newnode = l1
        ptr = newnode
        l1 = l1.next
        while(l1 and l2):
            if l1.val > l2.val:
                l2, l1 = l1, l2
            
            ptr.next = l1
            l1 = l1.next
            ptr = ptr.next
        
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2
        
        return newnode
        