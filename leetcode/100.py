# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p == None and q == None:
            return True
        
        result = True
        result = result and p.val == q.val
        
        result = result and self.isSameTree(p.left, q.left)
        result = result and self.isSameTree(p.right, q.right)
            
        return result
        