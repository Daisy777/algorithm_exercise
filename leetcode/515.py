'''Author:    ZHAO Zinan
Created: 12/04/2018

515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        # WFS use a queue
        queue = [root, None]
        maxele = []
        level = 1
        while len(queue) > 1:
            while(queue[0] != None):
                i = queue[0]

                if len(maxele) < level:
                    maxele.append(i.val)
                else:
                    maxele[level-1] = max(maxele[level-1], i.val)
                
                if i.left:
                    queue.append(i.left)

                if i.right:
                    queue.append(i.right)

                queue.pop(0)
            queue.pop(0)
            level += 1
            queue.append(None)

        return maxele


# test
if __name__ == '__main__':
    a = TreeNode(1)

    b = TreeNode(3)
    c = TreeNode(2)

    a.left = b
    a.right = c

    d = TreeNode(5)
    e = TreeNode(3)
    f = TreeNode(9)

    b.left = d
    b.right = e
    c.right = f

    print(Solution().largestValues(a))

            