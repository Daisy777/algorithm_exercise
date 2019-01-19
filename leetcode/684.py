'''
Author:    ZHAO Zinan
Created: 01/19/2019

684. Redundant Connection
'''
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        class Node:
            def __init__(self, val, parent=None):
                self.parent = parent
                self.val = val
            def root(self):
                root = self
                while(root.parent):
                    root = root.parent
                return root
        class Disjoint:
            def __init__(self, n):
                self.nodes = [Node(i) for i in range(n)]
            
            def check(self, a, b):
                if self.nodes[a-1].root() == self.nodes[b-1].root():
                    return False
                return True
            def join(self, a, b):
                # I don't care about the performace here ...
                self.nodes[a-1].root().parent = self.nodes[b-1].root()

        n = len(edges)
        disjoint = Disjoint(n)
        for edge in edges:
            if not disjoint.check(edge[0], edge[1]):
                return edge
            
            disjoint.join(edge[0], edge[1])


# test
if __name__ == '__main__':
    print(Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
    # [1, 4]
    print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]))
    # [2, 3]
