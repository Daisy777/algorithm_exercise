'''
Author: ZHAO Zinan
Created: 10. March 2019

1008. Construct Binary Search Tree from Preorder Traversal
''' 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

            
class Solution:
    def _bstFromPreorder(self, preorder: List[int], begin: int, end:int) -> TreeNode:
        if end < begin:
            return None
        if end == begin:
            return TreeNode(preorder[begin])
        
        root = preorder[begin]
        rootNode = TreeNode(root)
        middle = end+1
        for index, node in enumerate(preorder[begin+1:end+1]):
            if node > root:
                middle = index+begin+1
                break
        
        rootNode.left = self._bstFromPreorder(preorder, begin+1, middle-1)
        rootNode.right = self._bstFromPreorder(preorder, middle, end)
        return rootNode
        
            
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        return self._bstFromPreorder(preorder, 0, len(preorder)-1)
    
    
            