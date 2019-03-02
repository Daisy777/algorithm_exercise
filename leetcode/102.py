'''
Author: ZHAO Zinan
Created: 02. March 2019

102. Binary Tree Level Order Traversal
''' 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [(root, 1)]
        result = []
        while(queue):
            node, height = queue.pop(0)
            if height > len(result):
                result.append([])
            result[height-1].append(node.val)
            
            if node.left:
                queue.append((node.left, height+1))
            if node.right:
                queue.append((node.right, height+1))
            
        return result