# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root:'TreeNode') -> 'int':
        if not root:
            return 0
        def height(root):
            if not root:
                return -1
            return 1+height(root.left)
        
        h = height(root)
        if h == height(root.right)+1:
            return (1 << h) + self.countNodes(root.right)
        return (1 << (h-1)) + self.countNodes(root.left)

