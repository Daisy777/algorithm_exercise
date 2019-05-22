'''
Author:    ZHAO Zinan
Created: 22-May-2019

98. Validate Binary Search Tree
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# all the children nodes in the right tree should be larger than root value
from typing import List 

# all the children nodes in the right tree should be larger than root value
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True 

        def _isValidBST(root: TreeNode, lower: int, upper: int) -> bool:
            if not root:
                return True 
            if not (root.val < upper and root.val > lower):
                return False
            
            if root.left and root.right:
                return _isValidBST(root.left, lower, min(upper, root.val)) and _isValidBST(root.right, max(lower, root.val), upper) 
            if root.left:
                return _isValidBST(root.left, lower, min(upper, root.val)) 
            if root.right:
                return _isValidBST(root.right, max(lower, root.val), upper) 
            return True
        
        return _isValidBST(root.left, float('-inf'), root.val) and _isValidBST(root.right, root.val, float('inf')) 
 