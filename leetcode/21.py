# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if not self.next:
            return str(self.val)

        return str(self.val) + str(self.next)

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        pointer1 = l1
        pointer2 = l2
        head = pointer1
        if pointer1.val > pointer2.val:
            temp = pointer1
            pointer1 = pointer2
            pointer2 = temp

        while (pointer1.next and pointer2.next):
            if (pointer2.val >= pointer1.val and pointer2.val < pointer1.next.val):
                # insert pointer2 to pointer1.next
                temppointer = pointer2
                pointer2 = pointer2.next
                temppointer.next = pointer1.next
                pointer1.next = temppointer

            elif (pointer2.val > pointer1.next.val):
                pointer1 = pointer1.next
        
        if not
        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    c = ListNode(4)
    b.next = c

    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(4)
    d.next = e
    e.next = f

    print(Solution().mergeTwoLists(a, d))