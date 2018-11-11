# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        init_head = head
        previous = None
        insert_head = head

        while head:
            if head.val < x:
                # remove from previous location
                temp_pointer = head
                head = head.next
                if previous:
                    previous.next = head

                # insert to the next location
                temp_pointer.next = insert_head.next
                insert_head.next = temp_pointer
                insert_head = insert_head.next
                
            else:
                head = head.next
                
            previous = head
            

        return init_head

# test
if __name__=='__main__':
    head = ListNode(3)
    Solution().partition()