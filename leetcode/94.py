# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder_list = []
        if root == None:
            return inorder_list

        if root.left != None:
            inorder_list.extend(self.inorderTraversal(root.left))
        
        inorder_list.append(root.val)

        if root.right != None:
            inorder_list.extend(self.inorderTraversal(root.right))

        return inorder_list


