# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0

        if root.left and root.right:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
        elif root.left:
            return self.countNodes(root.left) + 1
        return 1
