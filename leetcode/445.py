'''
Author: ZHAO Zinan
Created: 11. April 2019

445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single
digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

''' 
def printlinked(resultnode):
    while(resultnode!=None):
        resultnode = resultnode.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x, nextn=None):
#         self.val = x
#         self.next = nextn

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getnumber(l1):
            if l1 == None:
                return 0
            ptr = l1
            num = 0
            while(ptr):
                num *= 10
                num += ptr.val
                ptr = ptr.next
            return num
        
        num1 = getnumber(l1)
        num2 = getnumber(l2)

        resultnum = num1+num2
        head = None
        while(resultnum>0):
            node = ListNode(resultnum%10)
            node.next = head
            head = node
            resultnum //=10
        if head == None:
            head = ListNode(0)
        return head
    
# test
if __name__ == '__main__':
    node1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    node2 = ListNode(5, ListNode(6, ListNode(4)))

    resultnode = Solution().addTwoNumbers(node1, node2)
    