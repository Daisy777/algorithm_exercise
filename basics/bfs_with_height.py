# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        q = [ (root, 1) ]
        ret = []
        if root == None:
            return ret
        
        while len(q) > 0:
            n, l = q.pop(0)
            if len(ret) < l:
                ret.append([])
                
            ret[l-1].append(n.val)
            

            if n.right != None:
                q.append((n.right, l+1))
            if n.left != None:
                q.append((n.left, l+1))
        return ret