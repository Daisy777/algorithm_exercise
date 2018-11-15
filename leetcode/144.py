'''
Author:    ZHAO Zinan
Created: 14-Nov-2018

144. Binary Tree Preorder Traversal
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        traversalVal = []
        traversalVal.append(root.val)

        if (root.left):
            traversalVal.extend(self.preorderTraversal(root.left))
        if (root.right):
            traversalVal.extend(self.preorderTraversal(root.right))

        return traversalVal

# test
if __name__ == '__main__':
    # test case 1
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(1)
    c.right = b
    b.left = a
    print(Solution().preorderTraversal(c))

    # test case 2
    d = TreeNode(1)
    e = TreeNode(4)
    f = TreeNode(3)
    g = TreeNode(2)
    d.left = e
    d.right = f
    e.left = g
    print(Solution().preorderTraversal(d))
    