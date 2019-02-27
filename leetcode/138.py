'''
Author: ZHAO Zinan
Created: 27. February 2019

https://leetcode.com/problems/copy-list-with-random-pointer/
''' 
# Definition for a Node.
# class Node:
#     def __init__(self, val, next, random):
#         self.val = val
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # traverse the linked list twice
        newhead = Node(head.val, None,None)
        ptr1 = head
        ptr2 = newhead
        address_book = {}
        address_book[id(head)] = newhead

        # create a linked list with all random = None
        while(ptr1.next):
            nextnode = Node(ptr1.next.val, None, None)
            address_book[id(ptr1.next)] = nextnode
            ptr2.next = nextnode
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        ptr1 = head
        ptr2 = newhead
        # refresh the random attribute
        while(ptr1):
            if ptr1.random == None:
                ptr2.random = None
            else:
                ptr2.random = address_book[id(ptr1.random)]
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return newhead
