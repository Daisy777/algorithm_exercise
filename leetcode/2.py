# Author: ZHAO Zinan
# Question Url: https://leetcode.com/problems/add-two-numbers/description/
# Date: 07-07-2018
#-----------------------------------------------------------------

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

 Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nextnode=None):
        self.val = x
        self.next = nextnode

    def __str__(self):
        return str(self.val)+"->"+str(self.next)

class Solution:
    @classmethod
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # to record whether need to +1 in the next digit
        flag = False
        x = l1

        while(l1.next!=None and l2.next!=None): 
            add = (1+l2.val) if flag == True else l2.val
            l1.val += add

            flag = False
            # change flag for the next loop
            if l1.val >= 10:
                flag = True
                l1.val = l1.val%10

            l1 = l1.next
            l2 = l2.next


        if l1 == None and l2 != None:
            l1 = l2
        elif l1 == None and l2 == None and flag == True:
            l1.next = ListNode(1)

        return x

if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(5)
    print(Solution.addTwoNumbers(l1, l2))

