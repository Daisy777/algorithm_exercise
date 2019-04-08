'''
Author: ZHAO Zinan
Created: 08. April 2019

426. Convert Binary Search Tree to Sorted Doubly Linked List
Convert a BST to a sorted circular doubly-linked list in-place. 
Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
''' 

# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if not root:
        return []
    result = []
    result.extend(inorder(root.left))
    result.append(root)
    result.extend(inorder(root.right))
    return result

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
            
        inordernodes = inorder(root)
        lennode = len(inordernodes)

        head = inordernodes[0]
        for i in range(lennode-1):
            inordernodes[i].right = inordernodes[i+1]
            inordernodes[i+1].left = inordernodes[i]
        inordernodes[-1].right = head
        head.left  = inordernodes[-1]
        return head
# test
if __name__ == '__main__':
    b = Node(1, None, None)
    d = Node(3, None, None)
    c = Node(2, b, d)
    e = Node(5, None, None)
    g = Node(7, None, None)
    f = Node(6, e, g)
    a = Node(4, c, f)
    def printdoublelinkedtree(head):
        print(head.val)
        ptr = head.right
        while(ptr!=head):
            print(ptr.val)
            ptr = ptr.right

    # inordernodes = inorder(a)
    # for i in range(len(inordernodes)):
    #     print(inordernodes[i].val)

    printdoublelinkedtree(Solution().treeToDoublyList(a))
