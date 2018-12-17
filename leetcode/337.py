'''
Author:    ZHAO Zinan
Created: 12/17/2018

337. House Robber III
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robBTDepth(root, depth):
            if depth==0:
                return 0
            if depth == 1:
                return root.val;

            # sum of child
            sumchild = 0
            if root.left:
                sumchild += root.left.val
            if root.right:
                sumchild += root.right.val

            n = 3
            ndepthchild = [root, None]
            for i in range(2):
                node = ndepthchild.pop(0)
                while node:
                    if node.left:
                        ndepthchild.append(node.left)
                    if node.right:
                        ndepthchild.append(node.right)
                    node = ndepthchild.pop(0)

                ndepthchild.append(None)
                

            nodes = list(zip(ndepthchild, [1]*len(ndepthchild))) if root.val > sumchild else list(zip(ndepthchild, [0]*len(ndepthchild)))
            result = [root.val, max(root.val, sumchild)]

            while (n<=depth):
                sumn = 0
                sum1n = 0
                for node in nodes:
                    if node[0]:
                        sumn += node[0].val
                        if node[1]:
                            sum1n += node[0].val

                result_n_min_2 = result[(n-1)%2] + sumn
                result_n_min_1 = result[n%2] + sum1n



                n += 1                
                if n <= depth:
                    # add next level's nodes
                    if result_n_min_2 > result_n_min_1:
                        result[n%2] = result_n_min_2
                        node = nodes.pop(0)
                        while node[0]:
                            if node[0].left:
                                nodes.append((node[0].left, 1)) 
                            if node[0].right:
                                nodes.append((node[0].right, 1)) 
                            node = nodes.pop(0)
                                
                        nodes.append((None, 0))
                    else:
                        result[n%2] = result_n_min_1
                        node = nodes.pop(0)
                        while node[0]:
                            if node[0].left:
                                nodes.append((node[0].left, node[1]^1)) 
                            if node[0].right:
                                nodes.append((node[0].right, node[1]^1)) 
                            node = nodes.pop(0)
                                
                        nodes.append((None, 0))
                else:
                    return max(result_n_min_1, result_n_min_2)

        # cal depth
        def maxDepth(root):
            if not root:
                return 0
            leftdepth = maxDepth(root.left)
            rightdepth = maxDepth(root.right)
            return max(1+leftdepth, 1+rightdepth)

        depth = maxDepth(root)
        return robBTDepth(root, depth)

# test
if __name__ == '__main__':
    # test1
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(3)
    e = TreeNode(1)

    a.left = b
    a.right = c
    b.right = d
    c.right = e
    print(Solution().rob(a)) # 7               