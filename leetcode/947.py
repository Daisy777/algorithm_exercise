'''
Author: ZHAO Zinan
Created: 19. February 2019

https://leetcode.com/problems/most-stones-removed-with-same-row-or-column
tags: union find
''' 
class Solution:
    def removeStones(self, stones: 'List[List[int]]') -> 'int':
        # disjoint set?
        class UnionFind:
            def __init__(self):
                self.uf = {}

            def union(self, x, y):
                self.uf.setdefault(x, x)
                self.uf.setdefault(y, y)
                if not self.connected(x, y):
                    self.uf[self.find(x)] = y

            def find(self, x):
                if (self.uf[x] == x):
                    return x
                return self.find(self.uf[x])

            def connected(self, x, y):
                return self.find(x) == self.find(y)

        uf = UnionFind()
        for x, y in stones:
            uf.union(x, ~y)
        return len(stones) - len({uf.find(x) for x in uf.uf})

# test
if __name__ == '__main__':
    print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])) # 5
    print(Solution().removeStones( [[0,0],[0,2],[1,1],[2,0],[2,2]])) # 3
    print(Solution().removeStones([(0,0)])) # 0
    print(Solution().removeStones([[3,2],[0,0],[3,3],[2,1],[2,3],[2,2],[0,2]]))
