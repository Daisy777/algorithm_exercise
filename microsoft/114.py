# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def _flatten(root, tail):
            if not root:
                return 

            if not root.left and not root.right:
                return root
            if not root.left:
                tail = _flatten(root.right)
                return tail
            
            tail = _flatten(root.left)
            _flatten(root.right)
            tail.right = root.right
            root.right = root.left
            root.left = None

        _flatten(root)