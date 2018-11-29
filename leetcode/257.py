'''
Author:    ZHAO Zinan
Created: 11/28/2018

257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        # recursion
        if not root.left and not root.right:
            return [str(root.val)]

        result = []
        if root.left:
            result.extend([''.join([str(root.val), '->', child]) for child in self.binaryTreePaths(root.left)])
            
        if root.right:
            result.extend([''.join([str(root.val), '->', child]) for child in self.binaryTreePaths(root.right)])

        return result

if __name__ == '__main__':
    a = TreeNode(0)
    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)

    a.left = b
    b.left = e
    b.right  = c
    a.right = d
    print(Solution().binaryTreePaths(a))