'''
Author: ZHAO Zinan
Created: 26. February 2019

938. Range Sum of BST
''' 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _inorder(self, node, L, R):
        sum = 0
        if not node:
            return sum

        '''
        we can stop early 
        node.val < L, no need to traverse left child tree
        node.val > R, no need to traverse right child tree
        '''
        if node.val > L:
            sum += self._inorder(node.left, L, R)
        if node.val >= L and node.val <= R:
            sum += node.val
        if node.val < R:
            sum += self._inorder(node.right, L, R)
        return sum
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # inorder traverse as it follows the order of elements
        return self._inorder(root, L, R)        

# test
if __name__ == '__main__':
    print(Solution().rangeSumBST())